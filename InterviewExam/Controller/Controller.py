#import __init__
from DAL import DataAccessLayer as dal
from Controller.InputConverter import convert_to_dict

def empty_output_validation(tickets_list):
    if len(tickets_list)>0:
        return {"tickets": tickets_list}
    else:
        return {"message": "No matched tickets"}

def output_gate(tickets_list):
    return empty_output_validation(tickets_list)

def get_all_tickets():
    '''this function returns all tickets'''
    tickets = dal.load_database()
    return output_gate(tickets)
    
def tickets_text_filter(query):
    '''This function returns all tickets that match text field-content from the list [(text field,searched content)]'''
    query_dict = convert_to_dict(query)
    print(query_dict)
    print(type(query_dict))
    tickets = dal.filter_by_txt(query_dict)
    return output_gate(tickets)

def ticket_time_filter(query):
    '''This function returns all the tickets in the time frame'''
    query_dict = convert_to_dict(query)
    tickets = dal.filter_by_time(query_dict)
    return output_gate(tickets)



