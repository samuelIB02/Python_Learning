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



#Exercise 4,5 and 6: Learning json.load() method + addding a try/except to handle excpetions + Checking result before using them
def load_config():
    try:
        with open("config.json", "r", encoding="utf-8") as file:
            result = json.load(file)

        return result
    except (FileNotFoundError,json.JSONDecodeError):
        return None

config = load_config()
if config is not None:
    print(config["model"])
    print(config["temperature"])
    print(type(config))
else:
    print("Configuration could not be loaded")


#Exercise 6: Accesing an incomplete dictionary

config_incomplete = {
    "model": "gpt-example",
    "temperature": 0.7
}

def get_max_tokens(config_incomplete):
    max_tokens = config_incomplete.get("max_tokens",1000)

    return max_tokens

print(get_max_tokens(config_incomplete))
   

