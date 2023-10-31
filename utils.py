import json

def load_json(path):
    try:
        with open(path, "r") as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(e)