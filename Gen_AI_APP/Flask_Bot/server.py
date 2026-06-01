# ============================================================
# FastAPI + Gemini Backend
# ============================================================

import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai

# ============================================================
# Load .env
# ============================================================

load_dotenv()

# ============================================================
# Gemini Client
# ============================================================

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ============================================================
# FastAPI App
# ============================================================

app = FastAPI()

# ============================================================
# Request Model
# ============================================================

class QuestionRequest(BaseModel):
    question: str

# ============================================================
# Home Route
# ============================================================

@app.get("/")
def home():
    return {"message": "Gemini Backend Running"}

# ============================================================
# Ask Route
# ============================================================

@app.post("/ask")
def ask(data: QuestionRequest):

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=data.question
        )

        return {
            "success": True,
            "response": response.text
        }

    except Exception as e:

        return {
            "success": False,
            "response": str(e)
        }
