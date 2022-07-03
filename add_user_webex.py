#!/usr/bin/env python
# Author - omz - 13/04/2020

# below packages can be installed from pip 
# pip install requests json 
import requests
import json
from main import send_email

# Define Method to post data to API
def person_post(url, data):
    response = requests.post(url, data=json.dumps(data),
                                  headers={"Accept" : "application/json",
                                    "Content-Type":"application/json",
                                    "Authorization": "Bearer "+bearer})
    return response

################### REPLACE ##############################
#each user on a new line. no last blank line.
filepath = "user_email.txt" 
# room to add new users
room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMDU2NDZhYTAtZjlkNS0xMWVjLWIyYTEtZjdlZWRiZjUyMDhm" 
# add webex api admin token 
bearer = "NjhhZmNmMjktZjE1Mi00Y2M1LTliYmMtY2U0MjJlMDVhMjNhY2M1NjE1ZjItZGQ1_P0A1_cb008300-30e9-4832-8402-b7f63db3150c"
##########################################################

# empty list to hold the email addresses
emails = []
# open file to read the email addresses
with open(filepath, 'r') as read_emails:
    emails = read_emails.readlines()

# uncomment below line to check emails addresses are read from the text file
# print (emails)

# url to add new user to the room
add_membership_url = 'https://api.ciscospark.com/v1/memberships'

print
for email in emails: # every email address in the lines list
    try:
        param = {
        "roomId": room_id,
        "personEmail": email,
    }   

        # strip off any carriage return or new line characters from email
        person_email = email.strip('\r\n')

        # call the person_post method with 2 parameters, add_membership_url and payload
        result = person_post(add_membership_url,param)
        
        #print(result.status_code)

        if result.status_code == 409:
            print("{} - is already in the room.".format(person_email))
        elif result.status_code == 200:
            print("{} - is successfully added to the room.".format(person_email))
            send_email(person_email)
        else:
            result.json()
            print(result.status_code, result['message'])
        
        # uncomment below to see what error message is sent from the api
        #print(result.json())

    except Exception as e:
        print(e)
print