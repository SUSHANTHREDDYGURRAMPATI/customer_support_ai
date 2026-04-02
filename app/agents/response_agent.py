from services.llm_service import call_llm
from services.vector_store import search_docs

def generate_response(query, intent, user_data):
    context = search_docs(query)

    prompt = f"""
    You are a customer support assistant.

    Context: {context}
    User Data: {user_data}
    Query: {query}

    Generate accurate response.
    """

    return call_llm(prompt)