from App.services.gemini_service import generate_response


def job_search_agent(message: str):
    """
    Job Search AI Agent
    Receives user message and gets response from Gemini.
    """

    prompt = f"""
You are a professional Job Search AI Assistant.

Your responsibilities:
- Help users search for jobs.
- Answer career-related questions.
- Suggest interview tips.
- Help improve resumes.
- Provide professional guidance.

User Question:
{message}
"""

    response = generate_response(prompt)

    return response