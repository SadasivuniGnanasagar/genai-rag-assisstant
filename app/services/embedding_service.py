import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def generate_embedding(text):

    response = genai.embed_content(
        model="models/embedding-001",
        content=text
    )

    return response["embedding"]