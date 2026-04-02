from fastapi import FastAPI
from models.schemas import QueryRequest, QueryResponse

from agents.intent_agent import classify_intent
from agents.retrieval_agent import fetch_user_data
from agents.response_agent import generate_response
from agents.decision_agent import decide_action

from services.logger import log_event   # ✅ ADD THIS

app = FastAPI(title="Agent-Based Customer Support System")


@app.post("/handle_query", response_model=QueryResponse)
def handle_query(request: QueryRequest):

    # 🔹 Log incoming query
    log_event(f"Query: {request.query}")

    # Step 1: Intent
    intent = classify_intent(request.query)
    log_event(f"Intent: {intent}")   # ✅ AFTER intent

    # Step 2: Fetch user data
    user_data = fetch_user_data(request.user_id)

    if user_data is None:
        log_event("User not found")   # ✅ IMPORTANT
        return QueryResponse(
            intent="unknown_user",
            response="User not found in our system.",
            status="escalated"
        )

    # Step 3: Generate response
    response = generate_response(request.query, intent, user_data)

    # Step 4: Decision
    decision = decide_action(intent, response)

    if decision == "escalate":
        final_response = "Your issue has been escalated to a human agent."
        status = "escalated"
    else:
        final_response = response
        status = "resolved"

    # 🔹 Final logs
    log_event(f"Status: {status}")   # ✅ AFTER decision

    return QueryResponse(
        intent=intent,
        response=final_response,
        status=status
    )