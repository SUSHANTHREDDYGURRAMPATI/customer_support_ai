from fastapi import FastAPI
from models.schemas import QueryRequest, QueryResponse

from agents.intent_agent import classify_intent
from agents.retrieval_agent import fetch_user_data
from agents.response_agent import generate_response
from agents.decision_agent import decide_action
from models.schemas import QueryRequest, QueryResponse

app = FastAPI(title="Agent-Based Customer Support System")


@app.post("/handle_query", response_model=QueryResponse)
def handle_query(request: QueryRequest):
    # Step 1: Intent Classification
    intent = classify_intent(request.query)

    # Step 2: Fetch User Data
    user_data = fetch_user_data(request.user_id)

    # Step 3: Generate Response
    response = generate_response(request.query, intent, user_data)

    # Step 4: Decision
    decision = decide_action(intent, response)

    if decision == "escalate":
        final_response = "Your issue has been escalated to a human agent."
        status = "escalated"
    else:
        final_response = response
        status = "resolved"

    return QueryResponse(
        intent=intent,
        response=final_response,
        status=status
    )