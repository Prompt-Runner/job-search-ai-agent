from App.agents.job_search_agent import job_search_agent

def process_message(message: str):
    """
    Processes the user message and sends it to the Job Search Agent.
    """
    response = job_search_agent(message)

    return {
        "success": True,
        "response": response
    }