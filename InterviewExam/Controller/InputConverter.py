import json

def convert_string(inp):
    dict = json.loads(inp)
    return dict

def convert_by_type(inp,type):
    if type==str:
        dict = convert_string(inp)
        return dict
    print("Can't convert input to dictionary\json")
    return {"message": "Can't convert input to dictionary"}

def convert_to_dict(inp):
    t = type(inp)
    dict = convert_by_type(inp,t)
    return dict
