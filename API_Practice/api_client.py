import requests
from authentication import get_auth_headers


BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# GET
def get_post(post_id):
    url = f"{BASE_URL}/{post_id}"
    try:
        response = requests.get(url,timeout=10)
        response.raise_for_status()
        data = response.json()
        return data

    except requests.exceptions.RequestException:
        return None

#POST
def create_post(title, body, user_id):
    new_post = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    try:
        response = requests.post(BASE_URL,json=new_post, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data

    except requests.exceptions.RequestException:
        return None

# PUT
def update_post(post_id, title, body, user_id):
    url = f"{BASE_URL}/{post_id}"
    new_post = {
        "id": post_id,
        "title": title,
        "body": body,
        "userId": user_id
    }
    try:
        response = requests.put(url,json=new_post,timeout=10)
        response.raise_for_status()
        data = response.json()
        return data

    except requests.exceptions.RequestException:
        return None


# DELETE

def delete_post(post_id):
    url = f"{BASE_URL}/{post_id}"
    try:
        response = requests.delete(url,timeout=10)
        response.raise_for_status()
        return True

    except requests.exceptions.RequestException:
        return False

# Sending personalized HTTP headers + adding request authentication 

def get_request_headers():

    url = "https://httpbin.org/headers"

    fake_api_key = "demo-token-123"

    headers = {
        "X-App-Name": "PythonLearning",
        "Accept": "application/json",
        "Authorization": f"Bearer {fake_api_key}"
    }
    try:
        response = requests.get(url,headers=headers,timeout=10)
        response.raise_for_status()
        data = response.json()
        return data

    except requests.exceptions.RequestException:
        return None

# Authentication integration with requests

def fetch_authenticated_data(url):
    headers = get_auth_headers()

    if headers is not None:
        try:
            response = requests.get(url, headers=headers,timeout=10)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException:
            return None
    return None

