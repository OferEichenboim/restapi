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

q0 = {"text":{"id": "ab6fc754-0e01-5cfb-84b9-cf37c1c0cdb5","title": "How to Display Numbers with a Comma Separator"}}
q1 = {"text":{"title": "company Code Forum - Guidelines for posting a question", "userEmail": "kekikum@segtaj.gh"}}
q2 = {"text":{"content": "Hi there!\n\nI just want to ask how to fix my problem regarding on my login page.\n\nI watched and followed a tutorial on how to make database and a login page, here's what I have done following the tutorial, I did not mean to say it is wrong but I think I lack of something that I cannot decode on myself and I have a hard time looking since I am not sure what it is.\n\nHere is what I did:\n\n* Database collection\n* A pagecontent where there is:\n\nFirst Name\nLast Name\nEmail\nUpload Profile\nAbout Me\n\nThis page is connected to my database which I did right\n\n* I made a dynamic page wherein it will show the content that I will write from the page content I mentioned above. If I will not write information on that page content, my dynamic page will be blank.\n\nAfter I created a database, a page and a dynamic page, I, then created the login/logout page using codes.\n\nMy concern is this, once I click on my profile, instead of going to my dynamic page, it should be on my page content. Once I put information on that page, then it will show my dynamic page.\nHow can I, or what should I do with that?\n\nThank you for the answers.\n"}}

print("Should be 0 tickets: ",filter_by_txt(q0))
print("Should be one ticket: ",len(filter_by_txt(q1)))
print("Should be one ticket: ",len(filter_by_txt(q2)))