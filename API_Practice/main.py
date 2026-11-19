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
