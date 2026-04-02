def decide_action(intent: str, response: str):
    if intent == "unknown":
        return "escalate"

    if len(response) < 20:
        return "escalate"

    return "resolve"