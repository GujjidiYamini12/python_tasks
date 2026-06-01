import os
from flask import Flask, request, render_template_string
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)

# ============================================================
# GEMINI CLIENT
# ============================================================

def get_client():
    return genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# ✅ SAFE MODEL LIST (fixes 404 issues)
MODELS = [
    "gemini-2.0-flash",
    "gemini-1.5-flash-latest",
    "gemini-1.5-pro-latest"
]

# ============================================================
# GEMINI CALL (SAFE + FALLBACK)
# ============================================================

def ask_gemini(question: str):
    client = get_client()

    for model in MODELS:
        try:
            print("✅ Using model:", model)

            response = client.models.generate_content(
                model=model,
                contents=question
            )
            return response.text

        except Exception as e:
            print("⚠️ Model failed:", model, e)

            # Handle quota error cleanly
            if "429" in str(e):
                return "⚠️ Daily quota finished. Please try again later or upgrade your API plan."

            continue

    return "⚠️ All AI models failed. Please try again later."

# ============================================================
# CHAT HISTORY
# ============================================================

chat_history = []

# ============================================================
# HTML + CSS (CHAT UI)
# ============================================================

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Chatbot</title>
    <style>
        body {
            background: #0f172a;
            font-family: Arial;
            margin: 0;
        }

        .container {
            width: 60%;
            margin: auto;
            margin-top: 30px;
        }

        h2 {
            color: white;
            text-align: center;
        }

        .chat-box {
            height: 70vh;
            overflow-y: auto;
            background: #111827;
            padding: 20px;
            border-radius: 10px;
            color: white;
        }

        .user {
            text-align: right;
            color: #60a5fa;
            margin: 10px;
            padding: 8px;
        }

        .bot {
            text-align: left;
            color: #34d399;
            margin: 10px;
            padding: 8px;
        }

        form {
            display: flex;
            margin-top: 10px;
        }

        input {
            flex: 1;
            padding: 12px;
            border: none;
            border-radius: 5px;
        }

        button {
            padding: 12px;
            margin-left: 10px;
            background: #2563eb;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background: #1d4ed8;
        }
    </style>
</head>

<body>

<div class="container">

    <h2>💬 AI Chatbot</h2>

    <div class="chat-box">

        {% for chat in history %}
            <div class="user">🧑 You: {{ chat.user }}</div>
            <div class="bot">🤖 Bot: {{ chat.bot }}</div>
        {% endfor %}

    </div>

    <form method="POST">
        <input type="text" name="question" placeholder="Ask something..." required>
        <button type="submit">Send</button>
    </form>

</div>

</body>
</html>
"""

# ============================================================
# FLASK ROUTE
# ============================================================

@app.route("/", methods=["GET", "POST"])
def home():
    global chat_history

    if request.method == "POST":
        question = request.form["question"]

        answer = ask_gemini(question)

        chat_history.append({
            "user": question,
            "bot": answer
        })

    return render_template_string(HTML_PAGE, history=chat_history)

# ============================================================
# RUN APP
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)
