def fetch_user_data(user_id: str):
    from database.mock_db import USER_DB
    
    user_data = USER_DB.get(user_id)

    if not user_data:
        return None   # IMPORTANT

    return user_data