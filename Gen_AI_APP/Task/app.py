import os
from flask import Flask, request, render_template_string
from dotenv import load_dotenv
import mysql.connector
from google import genai

# =========================
# LOAD ENV
# =========================
load_dotenv()

app = Flask(__name__)

# =========================
# DATABASE CONNECTION SAFE
# =========================
def get_db():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="movie_booking_db"
)

# create table safely every run
def init_db():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_msg TEXT,
            bot_msg TEXT
        )
    """)
    db.commit()
    cursor.close()
    db.close()

init_db()

# =========================
# GEMINI CLIENT
# =========================
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "gemini-1.5-flash"   # ⚠️ IMPORTANT: use valid model

# =========================
# GEMINI FUNCTION
# =========================
def ask_gemini(question):
    try:
        movie_prompt = f"""
        You are CineOrbit AI Assistant.

        You help users with:
        - Movie information
        - Show timings
        - Seat booking guidance
        - Ticket cancellation information
        - Movie recommendations
        - Theater facilities
        - Payment assistance

        User Question:
        {question}

        Give a friendly and concise response.
        """

        response = client.models.generate_content(
            model=MODEL,
            contents=movie_prompt
        )

        return response.text

    except Exception as e:
        print("AI Error:", e)
        return "⚠️ AI service unavailable. Please try again later."

# =========================
# SAVE CHAT
# =========================
def save_chat(user, bot):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO chat_history (user_msg, bot_msg) VALUES (%s, %s)",
        (user, bot)
    )
    db.commit()
    cursor.close()
    db.close()

# =========================
# GET CHAT HISTORY
# =========================
def get_history():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT user_msg, bot_msg FROM chat_history ORDER BY id")
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data

# =========================
# CHAT UI (CLEAN CHATBOT)
# =========================
HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Movie Management AI Chatbot</title>

<style>
body { background:#0f172a; font-family:Arial; }
.container { width:60%; margin:auto; margin-top:20px; }

.chat-box {
    height:70vh;
    overflow-y:auto;
    background:#111827;
    padding:20px;
    border-radius:10px;
    color:white;
}

.user { text-align:right; color:#60a5fa; margin:10px; }
.bot { text-align:left; color:#34d399; margin:10px; }

form { display:flex; margin-top:10px; }

input {
    flex:1;
    padding:12px;
    border:none;
    border-radius:5px;
}

button {
    padding:12px;
    margin-left:10px;
    background:#2563eb;
    color:white;
    border:none;
    border-radius:5px;
}
</style>

</head>

<body>

<div class="container">

<h2 style="color:white;text-align:center;">🎬 CineOrbit AI Assistant</h2>

<div class="chat-box">
{% for u,b in history %}
<div class="user">🧑 {{u}}</div>
<div class="bot">🤖 {{b}}</div>
{% endfor %}
</div>

<form method="POST">
<input name="question"
       placeholder="Ask about movies, bookings, tickets..."
       required>
<button type="submit">Send</button>
</form>

</div>

</body>
</html>
"""

# =========================
# ROUTE
# =========================
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        question = request.form["question"]

        answer = ask_gemini(question)

        save_chat(question, answer)

    history = get_history()
    return render_template_string(HTML, history=history)

# =========================
# RUN
# =========================
if __name__ == "__main__":
    app.run(debug=True)
