import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

def generate(question):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )


    model = "gemini-2.5-flash"

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=question),
            ],
        ),
    ]

    tools = [
        types.Tool(
            googleSearch=types.GoogleSearch()
        ),
    ]

    generate_content_config = types.GenerateContentConfig(
        tools=tools,
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if chunk.text:
            print(chunk.text, end="")


if __name__ == "__main__":
    question = input("Enter your question: ")
generate(question)
