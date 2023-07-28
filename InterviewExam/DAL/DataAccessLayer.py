#import __init__
import json


db_path = "Task_env/data.json"

def load_database(db = db_path):
    '''This function load the json database to a python list'''
    with open(db,"r",encoding="utf-8") as f:
        output = json.load(f)
    return output

def check_txt(ticket,text_dict):
    for key in text_dict.keys():
        if ticket[key] != text_dict[key]:
            return False
    return True

def add_match(out_list,add,ticket):
    if add == True:
        out_list.append(ticket)
    return out_list

def filter_by_txt(query_dict):
    output_list = []
    global db_list
    for ticket in db_list:
        add = check_txt(ticket,query_dict["text"])
        output_list = add_match(output_list,add,ticket)
    return output_list

def get_type_time(time_dict,type):
    if type=="start":
        t = time_dict["start"]
    elif type == "end":
        t = time_dict["end"]
    else:
        raise KeyError
    return t
    

def get_time(time_dict):
    start_time = 0
    end_time = 9999999999999
    if "start" in time_dict.keys():
        start_time = get_type_time(time_dict,"start")
    if "end" in time_dict.keys():
        end_time = get_type_time(time_dict,"end") 
    return start_time,end_time
    
        
def filter_by_time(query_dict):
    global db_list
    output_tickets = []
    if "time" in query_dict.keys():
        start_time,end_time = get_time(query_dict["time"]) 
    for ticket in db_list:
        if ticket["creationTime"]>=start_time and ticket["creationTime"]<=end_time:
            output_tickets.append(ticket)
    return output_tickets


db_list = load_database()