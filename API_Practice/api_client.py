import requests


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

