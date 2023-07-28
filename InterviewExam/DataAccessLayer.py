import json

db_path = "data.json"

def load_database(db = db_path):
    '''This function load the json database to a python list'''
    with open(db,"r",encoding="utf-8") as f:
        output = json.load(f)
    return output


def filter_by_txt(query_dict):
    idx_to_delete = set()
    output_list = []
    global db_list
    for key in query_dict["text"].keys():
        for i,ticket in enumerate(db_list):   
            if ticket[key]!=query_dict["text"][key]:
                idx_to_delete.add(i)
    for i in range(len(db_list)):
        if i not in idx_to_delete:
            output_list.append(db_list[i])
    return output_list

def get_query_time(time_dict,type):
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
        start_time = get_query_time(time_dict,"start")
    if "end" in time_dict.keys():
        end_time = get_query_time(time_dict,"end") 
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