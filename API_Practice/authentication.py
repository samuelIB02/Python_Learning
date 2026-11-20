import os
from dotenv import load_dotenv

def get_auth_headers():
    load_dotenv()

    api_key = os.getenv("API_KEY")

    if api_key is not None:
        return {
             "Authorization": f"Bearer {api_key}"
        }
    return None