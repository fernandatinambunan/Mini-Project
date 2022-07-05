import email
import smtplib
import ssl
from email.message import EmailMessage

def send_email(emails):
    #txt file containing the email password
    password = "sandi.txt"
    email_sender = 'nandatinambunan13@gmail.com'
    email_password =  password
    email_receiver = emails

    #contents of the subject field
    subject = 'Check out The Mini Project Space!'
    #contents of the body field
    body = """
    You just joined webex space. Go to the following links to get to know the people you work with.
    webexteams://im?space=05646aa0-f9d5-11ec-b2a1-f7eedbf5208f
    """

    mail = EmailMessage()
    mail['From'] = email_sender
    mail['To'] = email_receiver
    mail['Subject'] = subject
    mail.set_content(body)

    context = ssl.create_default_context()

    #use SMTP protocol 
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(mail)