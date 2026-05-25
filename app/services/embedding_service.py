import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing")

genai.configure(api_key=GOOGLE_API_KEY)

def generate_embedding(text):

    response = genai.embed_content(
        model="models/embedding-001",
        content=text
    )

    return response["embedding"]