import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API Key
API_KEY = os.getenv("GOOGLE_API_KEY")

# Validate API Key
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# Create Gemini Client
client = genai.Client(api_key=API_KEY)


def generate_response(prompt: str) -> str:
    """
    Generate AI response using Gemini.
    """

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        if hasattr(response, "text") and response.text:
            return response.text

        return "No response generated."

    except Exception as e:
        return f"Gemini Error: {str(e)}"


if __name__ == "__main__":
    print("===== Gemini AI Test =====")
    user_prompt = input("Enter your prompt: ")

    result = generate_response(user_prompt)

    print("\nGemini Response:\n")
    print(result)