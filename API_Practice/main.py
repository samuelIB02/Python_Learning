import requests


# First HTTP request

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url, timeout=10)

print(response.status_code)

data = response.json()

print(data["title"])

# Manage failed HTTP request

url_failed = "https://httpbin.org/status/404"

try:
    response_failed = requests.get(url_failed,timeout=10)
    response_failed.raise_for_status()
except requests.HTTPError:
    print("HTTP request failed")

# Managing different types of error

def fetch_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    # except requests.exceptions.RequestException: (handles all 3 exceptions)
    except (requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout
        ):
            return None

print(fetch_data(url))

# Checking responde before using it


data = fetch_data("https://jsonplaceholder.typicode.com/posts/1")
if data is not None:
    print(data["title"])
else:
    print("HTTP request failed")

# My first POST request + Checking POST results

new_post = {
    "title": "Learning Python APIs",
    "body": "My first POST request",
    "userId": 1
}

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.post(url, json=new_post, timeout=10)
    response.raise_for_status()
    if response.status_code == 201:
       print("Post created successfully")
       new_data = response.json()
       print(f"último ejercicio{new_data}")

    else:
        print("Unexpected status code")
       
except requests.exceptions.RequestException:
    print("POST request failed")

# Encapsulating a POST request

def create_post(title,body,user_id):
    new_post = {
    "title": title,
    "body": body,
    "userId": user_id
    }
    try:
        response = requests.post(url, json=new_post, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
       
    except requests.exceptions.RequestException:
        return None

# PATCH method

url = "https://jsonplaceholder.typicode.com/posts/1"

def update_post_title(post_id, new_title):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    new_post = {
        "title": new_title
    }
    try:
        response = requests.patch(url, json=new_post,timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
        
    except requests.exceptions.RequestException:
        return None

# DELETE method

def delete_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        response = requests.delete(url,timeout=10)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False



