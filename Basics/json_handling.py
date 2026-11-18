import json
from textwrap import indent


#Exercise 1: Transform json file into a dictionary
api_response = '''
{
    "models": [
        {
            "name": "model-alpha",
            "tokens": 1500,
            "active": true
        },
        {
            "name": "model-beta",
            "tokens": 3200,
            "active": false
        },
        {
            "name": "model-gamma",
            "tokens": 2800,
            "active": true
        }
    ]
}
'''

def get_active_models(api_response):
    models = json.loads(api_response)

    active_models = []

    for model in models["models"]:
        if model["active"]:
            active_models.append(model["name"])
    return active_models

print(get_active_models(api_response))

#Exercise 2: Transform a dictionary into a json file

request_data = {
    "model": "gpt-example",
    "temperature": 0.7,
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain Python dictionaries."}
    ]
}

def prepare_request(data):
    data_dump = json.dumps(data, indent=4)
    return data_dump

print(prepare_request(request_data))

#Exercise 3: Creating and saving a json file from a dictionary

config = {
    "model": "gpt-example",
    "temperature": 0.7,
    "max_tokens": 2000,
    "stream": False
}

def save_config(config):
    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(config,file, indent=4)



#Exercise 4: Learning json.load() method
def load_config():
    with open("config.json", "r", encoding="utf-8") as file:
        result = json.load(file)

    return result

config = load_config()

print(config["model"])
print(config["temperature"])
print(type(config))

#Exercise 5: Exception handling

