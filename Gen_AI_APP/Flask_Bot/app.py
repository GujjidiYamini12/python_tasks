
# ============================================================
# 🚀 Advanced GPT Style Flask Chat UI
# ============================================================

# Install Packages:
# pip install flask requests

from flask import Flask, render_template_string, request, jsonify
import requests

# ============================================================
# Flask App
# ============================================================

app = Flask(__name__)

# ============================================================
# FastAPI Backend URL
# ============================================================

FASTAPI_URL = "http://127.0.0.1:8000/ask"

# ============================================================
# HTML PAGE
# ============================================================

HTML_PAGE = """

<html>

<head>

<title>Gemini GPT Chat</title>

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Inter',sans-serif;
}

body{
    height:100vh;
    overflow:hidden;

    background:linear-gradient(
        -45deg,
        #0f172a,
        #1e1b4b,
        #111827,
        #312e81
    );

    background-size:400% 400%;
    animation:bgMove 12s ease infinite;
}

@keyframes bgMove{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

.chat-container{
    width:95%;
    max-width:1200px;
    margin:auto;
    height:100vh;
    display:flex;
    flex-direction:column;
}

.header{
    margin-top:15px;

    background:rgba(255,255,255,.05);

    backdrop-filter:blur(20px);

    border:1px solid rgba(255,255,255,.1);

    border-radius:20px;

    padding:20px;

    text-align:center;

    color:white;

    font-size:30px;

    font-weight:700;

    box-shadow:
    0 8px 32px rgba(0,0,0,.25);
}

.messages{
    flex:1;
    overflow-y:auto;
    padding:25px 10px;
    scroll-behavior:smooth;
}

.messages::-webkit-scrollbar{
    width:6px;
}

.messages::-webkit-scrollbar-thumb{
    background:#475569;
    border-radius:10px;
}

.message{
    display:flex;
    margin-bottom:25px;
    animation:fadeIn .4s ease;
}

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(20px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

.user{
    justify-content:flex-end;
}

.bot{
    justify-content:flex-start;
}

.icon{
    width:48px;
    height:48px;
    border-radius:50%;

    display:flex;
    justify-content:center;
    align-items:center;

    font-size:22px;

    margin:0 10px;
}

.user .icon{
    background:#2563eb;
    color:white;
}

.bot .icon{
    background:#10b981;
    color:white;
}

.bubble{
    max-width:70%;
    padding:18px 22px;

    line-height:1.7;

    border-radius:20px;

    color:white;

    word-break:break-word;

    transition:.3s;
}

.bubble:hover{
    transform:translateY(-2px);
}

.user .bubble{
    background:linear-gradient(
        135deg,
        #2563eb,
        #3b82f6
    );

    border-bottom-right-radius:8px;

    box-shadow:
    0 5px 20px rgba(37,99,235,.4);
}

.bot .bubble{
    background:rgba(255,255,255,.08);

    backdrop-filter:blur(15px);

    border:1px solid rgba(255,255,255,.08);

    border-bottom-left-radius:8px;
}

.input-box{
    padding:20px 0;
}

form{
    display:flex;
    gap:15px;
}

input{
    flex:1;

    padding:18px 22px;

    border:none;
    outline:none;

    border-radius:18px;

    background:rgba(255,255,255,.08);

    backdrop-filter:blur(15px);

    border:1px solid rgba(255,255,255,.1);

    color:white;

    font-size:16px;
}

input::placeholder{
    color:#94a3b8;
}

input:focus{
    border-color:#3b82f6;
    box-shadow:
    0 0 0 4px rgba(59,130,246,.2);
}

button{
    border:none;

    cursor:pointer;

    padding:18px 30px;

    border-radius:18px;

    color:white;

    font-size:15px;

    font-weight:600;

    background:linear-gradient(
        135deg,
        #2563eb,
        #4f46e5
    );

    transition:.3s;
}

button:hover{
    transform:translateY(-2px);

    box-shadow:
    0 10px 25px rgba(37,99,235,.35);
}

button:disabled{
    opacity:.6;
    cursor:not-allowed;
}

.typing{
    display:flex;
    align-items:center;
    gap:6px;
}

.dot{
    width:10px;
    height:10px;
    border-radius:50%;
    background:white;
    animation:typing 1.4s infinite;
}

.dot:nth-child(2){
    animation-delay:.2s;
}

.dot:nth-child(3){
    animation-delay:.4s;
}

@keyframes typing{
    0%,80%,100%{
        transform:scale(.5);
        opacity:.5;
    }
    40%{
        transform:scale(1);
        opacity:1;
    }
}

.footer{
    text-align:center;
    color:#94a3b8;
    padding-bottom:10px;
    font-size:13px;
}

</style>

</head>

<body>

<div class="chat-container">

    <div class="header">
        🤖 Gemini GPT Assistant
    </div>

    <div class="messages" id="messages">

    </div>

    <div class="input-box">

        <form id="chat-form">

            <input
                type="text"
                id="question"
                placeholder="Ask Gemini anything..."
                autocomplete="off"
                required
            >

            <button type="submit" id="send-btn">
                Send
            </button>

        </form>

    </div>

    <div class="footer">
        Powered by Gemini + FastAPI + Flask
    </div>

</div>

<script>

const form = document.getElementById("chat-form");
const input = document.getElementById("question");
const messages = document.getElementById("messages");
const sendBtn = document.getElementById("send-btn");

form.addEventListener("submit", async function(e){

    e.preventDefault();

    const question = input.value.trim();

    if(question === "") return;

    sendBtn.disabled = true;

    messages.insertAdjacentHTML(
        "beforeend",
        `
        <div class="message user">
            <div class="bubble">${question}</div>
            <div class="icon">👤</div>
        </div>
        `
    );

    const loadingId = "loading-" + Date.now();

    messages.insertAdjacentHTML(
        "beforeend",
        `
        <div class="message bot" id="${loadingId}">
            <div class="icon">🤖</div>

            <div class="bubble">
                <div class="typing">
                    <div class="dot"></div>
                    <div class="dot"></div>
                    <div class="dot"></div>
                </div>
            </div>
        </div>
        `
    );

    messages.scrollTop = messages.scrollHeight;

    input.value = "";

    try{

        const response = await fetch("/ask",{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                question:question
            })
        });

        const data = await response.json();

        document.getElementById(loadingId).innerHTML = `
            <div class="icon">🤖</div>
            <div class="bubble">
                ${data.response.replace(/\\n/g,"<br>")}
            </div>
        `;

    }
    catch(error){

        document.getElementById(loadingId).innerHTML = `
            <div class="icon">🤖</div>
            <div class="bubble">
                ${error}
            </div>
        `;
    }

    sendBtn.disabled = false;

    messages.scrollTop = messages.scrollHeight;

});

</script>

</body>

</html>

"""

# ============================================================
# Home Route
# ============================================================

@app.route("/")
def home():

    return render_template_string(HTML_PAGE)

# ============================================================
# API Route
# ============================================================

@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    question = data.get("question")

    try:

        response = requests.post(
            FASTAPI_URL,
            json={
                "question": question
            }
        )

        result = response.json()

        return jsonify({
            "response": result.get("response")
        })

    except Exception as e:

        return jsonify({
            "response": str(e)
        })

# ============================================================
# Run Flask App
# ============================================================

if __name__ == "__main__":

    app.run(debug=True, port=5000)
