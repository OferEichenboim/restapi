import json
import sys,os

def load_json_file(filename, encoding='utf-8'):
    try:
        with open(filename, 'r', encoding=encoding) as file:
            data = json.load(file)
        return data
    except FileNotFoundError as e:
        return "Not found"






