from App.services.gemini_service import generate_response
from App.services.retrieval_service import retrieve_context


def job_search_agent(message: str):
    """
    Resume RAG Job Search Agent
    """

    # Retrieve relevant resume context
    retrieved_chunks = retrieve_context(message)

    resume_context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are an AI Career Assistant.

Use ONLY the resume context below to answer.

If the answer is not available in the resume,
reply:

"I couldn't find that information in the uploaded resume."

=============================
Resume Context
=============================

{resume_context}

=============================
User Question
=============================

{message}

=============================
Answer
=============================
"""

    response = generate_response(prompt)

    return response