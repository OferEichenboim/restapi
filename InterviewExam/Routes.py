from fastapi import FastAPI
import Controller as ctrl
app = FastAPI()

@app.get("/")
def root():
    return {"message":"Welcome to the Company Exam, now emphasising SRP and devision to layers"}

@app.get("/tickets/txt_filter")
def get_ticket_by_title(query):
    return ctrl.tickets_text_filter(query)

@app.get("/tickets/time_filter")
def get_tickets_by_time(query):
    return ctrl.ticket_time_filter(query)

@app.get("/tickets/title_filter")
def get_ticket_by_title(query):
    return ctrl.tickets_text_filter(query)

@app.get("/tickets")
def get_tickets():
    return ctrl.get_all_tickets()

