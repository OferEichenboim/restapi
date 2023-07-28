
import os
import sys
import __init__
from DAL import DataAccessLayer 

q0 = {"text":{"id": "ab6fc754-0e01-5cfb-84b9-cf37c1c0cdb5","title": "How to Display Numbers with a Comma Separator"}}
q1 = {"text":{"title": "company Code Forum - Guidelines for posting a question", "userEmail": "kekikum@segtaj.gh"}}
q2 = {"text":{"content": "Hi there!\n\nI just want to ask how to fix my problem regarding on my login page.\n\nI watched and followed a tutorial on how to make database and a login page, here's what I have done following the tutorial, I did not mean to say it is wrong but I think I lack of something that I cannot decode on myself and I have a hard time looking since I am not sure what it is.\n\nHere is what I did:\n\n* Database collection\n* A pagecontent where there is:\n\nFirst Name\nLast Name\nEmail\nUpload Profile\nAbout Me\n\nThis page is connected to my database which I did right\n\n* I made a dynamic page wherein it will show the content that I will write from the page content I mentioned above. If I will not write information on that page content, my dynamic page will be blank.\n\nAfter I created a database, a page and a dynamic page, I, then created the login/logout page using codes.\n\nMy concern is this, once I click on my profile, instead of going to my dynamic page, it should be on my page content. Once I put information on that page, then it will show my dynamic page.\nHow can I, or what should I do with that?\n\nThank you for the answers.\n"}}

print("Should be 0 tickets: ",DataAccessLayer.filter_by_txt(q0))
print("Should be one ticket: ",len(DataAccessLayer.filter_by_txt(q1)))
print("Should be one ticket: ",len(DataAccessLayer.filter_by_txt(q2)))