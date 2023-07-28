import data_functions
from fastapi import FastAPI,status,HTTPException,Response
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class Ticket(BaseModel):
    id: str
    title: str
    content: str
    userEmail: str
    creationTime: int
    labels: list

tickets_list = data_functions.load_json_file("data.json") 

def find_ticket_by_title(title):
    '''This function search for a ticket by the title input and returns a list of matched tickets'''    
    match_tickets = []
    global tickets_list
    for tic in tickets_list:
        if tic["title"] == title:  
            match_tickets.append(tic)
    print(len(match_tickets)," tickets were found matching this query")
    return match_tickets

def find_ticket_by_time(start,end):
    '''Finds the tickets that were created during start-end time frame'''
    match_tickets = []
    global tickets_list
    for tic in tickets_list:
        if int(tic["creationTime"]) > int(start) and int(tic["creationTime"]) < int(end):  
            match_tickets.append(tic)
    print(len(match_tickets)," tickets were found matching this query")
    return match_tickets

def find_ticket_by_text_filter(title,content,email):
    global tickets_list
    match_tickets = tickets_list
    pop_idx = []
    correct_tickets = []
    if title!=None:
        for i,tic in enumerate(match_tickets):
            if tic["title"] != title:
                pop_idx.append(i)
    if content!=None:
        for i,tic in enumerate(match_tickets):
            if tic["content"] != content:
                if i not in pop_idx:
                    pop_idx.append(i)
    if email!=None:
        for i,tic in enumerate(match_tickets):
            if tic["userEmail"] != email:
                if i not in pop_idx:
                    pop_idx.append(i)
    for k in range(len(tickets_list)):
        if k not in pop_idx:
            correct_tickets.append(tickets_list[k])
    print(len(correct_tickets)," tickets were found matching this query")
    return correct_tickets

@app.get("/")
def root():
    return {"message":"Welcome to the interview API exam"}

#Solution to question 2 arranged by filter types
#all text fields filter
@app.get("/tickets/txt_filter") #todo: Improve path to exclude filter type
def get_ticket_by_txt_filter(title:str = None,content:str = None,email:str = None):
    '''Get the tickets matched the txt filters'''
    m_tickets = find_ticket_by_text_filter(title,content,email)
    if m_tickets == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"ticket with text fiter title = {title}, content = {content}, email = {email}, not found")
    return {"tickets":m_tickets}

#time filter
@app.get("/tickets/time_filter") #todo: Improve path to exclude filter type
def get_ticket_by_time(start_time=0,end_time=9999999999999):
    '''Get the tickets in the time frame from start to end time , default values based on the database'''
    m_tickets = find_ticket_by_time(start_time,end_time)
    if m_tickets == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"ticket with creation time between: {start_time} to {end_time} - was not found")
    return {"tickets":m_tickets}

#title filter
@app.get("/tickets/title_filter") #todo: Improve path to exclude filter type
def get_ticket_by_title(title:str):
    '''Get the tickets by the title'''
    m_tickets = find_ticket_by_title(title)
    if m_tickets == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"ticket with the title: {title} - was not found")
    return {"tickets":m_tickets}

#Solution to question 1
@app.get("/tickets")
def get_all_tickets():
    global tickets_list
    if type(tickets_list)==str:
        if tickets_list=="Not found":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"data.json file not found")
    return({"tickets":tickets_list})
