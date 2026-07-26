from App.agents.job_search_agent import job_search_agent


def process_message(message: str):
    """
    Workflow Layer
    """

    response = job_search_agent(message)

    return {
        "success": True,
        "response": response
    }