import json

def load_json(path):
    try:
        with open(path, "r", encoding='utf-8') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(e)