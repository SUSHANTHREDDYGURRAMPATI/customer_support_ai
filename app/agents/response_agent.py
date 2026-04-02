from services.llm_service import call_llm

def generate_response(query, intent, user_data):
    prompt = f"""
    You are a customer support assistant.

    User Query: {query}
    Intent: {intent}
    User Data: {user_data}

    Generate a helpful, accurate response.
    """

    return call_llm(prompt)