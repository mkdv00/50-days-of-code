import smtplib
import ssl
import os
from dotenv import load_dotenv


class Email:
    @staticmethod
    def send_email(message):
        load_dotenv()
        host = 'smtp.gmail.com'
        port = 465

        username = "maxim.cudaew@gmail.com"
        password = os.getenv('password')

        receiver = username
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)

        print("Email was sent!")
