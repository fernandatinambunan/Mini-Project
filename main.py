import smtplib
import ssl
from email.message import EmailMessage

def send_email(user_email):
    email_sender = 'nandatinambunan13@gmail.com'
    email_password = 'ckebqnnghjeqgrpn'
    email_receiver = user_email

    subject = 'Check out my new video!'
    body = """
    I've just published a new video on YouTube: https://youtu.be/2cZzP9DLlkg
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())