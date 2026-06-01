# ============================================================
# 🚀 FastAPI + Gemini + Full Frontend in Single File
# ============================================================

import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv

from google import genai

# ============================================================
# Load ENV
# ============================================================
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ============================================================
# FastAPI APP
# ============================================================
app = FastAPI()


# ============================================================
# Request Model
# ============================================================
class Question(BaseModel):
    question: str


# ============================================================
# HTML (Frontend UI)
# ============================================================
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Gemini Chat</title>

    <style>
        body{
            margin:0;
            font-family:Arial;
            background:#0f172a;
            color:white;
        }

        .container{
            max-width:800px;
            margin:auto;
            height:100vh;
            display:flex;
            flex-direction:column;
        }

        .header{
            padding:20px;
            text-align:center;
            font-size:24px;
            background:#111827;
        }

        .chat{
            flex:1;
            overflow-y:auto;
            padding:20px;
        }

        .msg{
            margin:10px 0;
            padding:12px 15px;
            border-radius:10px;
            max-width:70%;
        }

        .user{
            background:#2563eb;
            margin-left:auto;
            text-align:right;
        }

        .bot{
            background:#1e293b;
        }

        .input-box{
            display:flex;
            padding:15px;
            background:#111827;
        }

        input{
            flex:1;
            padding:12px;
            border:none;
            border-radius:8px;
            outline:none;
        }

        button{
            margin-left:10px;
            padding:12px 20px;
            border:none;
            border-radius:8px;
            background:#2563eb;
            color:white;
            cursor:pointer;
        }

        button:hover{
            background:#1d4ed8;
        }
    </style>
</head>

<body>

<div class="container">

    <div class="header">🤖 Gemini Chat (FastAPI)</div>

    <div class="chat" id="chat"></div>

    <div class="input-box">
        <input id="input" placeholder="Ask something..." />
        <button onclick="send()">Send</button>
    </div>

</div>

<script>

async function send(){

    let input = document.getElementById("input");
    let chat = document.getElementById("chat");

    let question = input.value;
    if(!question) return;

    // user message
    chat.innerHTML += `<div class="msg user">${question}</div>`;

    input.value = "";

    // loading
    let botDiv = document.createElement("div");
    botDiv.className = "msg bot";
    botDiv.innerHTML = "Thinking...";
    chat.appendChild(botDiv);

    chat.scrollTop = chat.scrollHeight;

    try{
        let res = await fetch("/ask", {
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body: JSON.stringify({question})
        });

        let data = await res.json();

        botDiv.innerHTML = data.response;

    }catch(err){
        botDiv.innerHTML = "Error: " + err;
    }

    chat.scrollTop = chat.scrollHeight;
}

</script>

</body>
</html>
"""


# ============================================================
# HOME PAGE
# ============================================================
@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_PAGE


# ============================================================
# CHAT API (Gemini)
# ============================================================
@app.post("/ask")
def ask(data: Question):

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=data.question
        )

        return {"response": response.text}

    except Exception as e:
        return {"response": str(e)}
