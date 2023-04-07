import smtplib, ssl
from dotenv import load_dotenv
import os


def send_email(message):
    load_dotenv()

    host = 'smtp.gmail.com'
    port = 465

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        username = os.getenv('USERNAME')
        receiver = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')

        server.login(username, password)
        server.sendmail(username, receiver, message)
