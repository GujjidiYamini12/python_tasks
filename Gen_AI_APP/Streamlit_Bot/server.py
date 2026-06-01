# ============================================================
# FastAPI + Gemini Backend (WORKING VERSION)
# ============================================================

import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

from google import genai   # NEW SDK

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

app = FastAPI()


# Request schema
class Question(BaseModel):
    question: str


# Health check
@app.get("/")
def home():
    return {"message": "Gemini FastAPI Running"}


# Chat endpoint
@app.post("/ask")
def ask(data: Question):

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=data.question
        )

        return {
            "response": response.text
        }

    except Exception as e:
        return {
            "response": f"Error: {str(e)}"
        }
