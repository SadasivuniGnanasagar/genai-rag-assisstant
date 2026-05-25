import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Configure Gemini API
genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Load Gemini model
model = genai.GenerativeModel(
    "gemini-flash-lite-latest"
)

def ask_llm(prompt):

    try:

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:

        error_message = str(e)

        # Handle quota errors
        if "429" in error_message:
            return (
                "Gemini API quota exceeded. "
                "Please wait for some time or use a new API key."
            )

        # Generic error
        return f"LLM Error: {error_message}"