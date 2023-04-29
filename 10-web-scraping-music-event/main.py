import requests
import selectorlib
import smtplib
import ssl
import os
from dotenv import load_dotenv

load_dotenv()


endpoint = 'http://programmer100.pythonanywhere.com/tours/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def scrape(url):
    """Scrape the page source from the url"""
    response = requests.get(url, headers=headers)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_email(message):
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


def store(extracted_data):
    with open('data.txt', 'a') as file:
        file.write(extracted_data + '\n')


def read():
    with open('data.txt', 'r') as file:
        return file.read()


if __name__ == '__main__':
    scraped = scrape(endpoint)
    extracted = extract(scraped)
    print(extracted)

    content = read()

    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted)
            send_email(message="Hey, new event was found!")
