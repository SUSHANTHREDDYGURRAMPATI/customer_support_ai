def decide_action(intent: str, response: str):
    if intent == "unknown":
        return "escalate"

    if "not sure" in response.lower():
        return "escalate"

    return "resolve"