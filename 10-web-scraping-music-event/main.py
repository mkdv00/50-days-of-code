import requests
import selectorlib
import smtplib
import ssl
import os
from dotenv import load_dotenv
import sqlite3
import time

load_dotenv()

endpoint = 'http://programmer100.pythonanywhere.com/tours/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

connection = sqlite3.connect('data.db')


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


def get_data():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events")
    result = cursor.fetchall()

    return result


def store_data(extracted_data):
    row_data = extracted_data.split(', ')
    row_data = [item.strip() for item in row_data]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row_data)
    connection.commit()


if __name__ == '__main__':
    scraped: str = scrape(endpoint)
    extracted = extract(scraped)
    print(extracted)

    content = get_data()

    if extracted[0] != "No upcoming tours":
        for row in content:
            if extracted not in row:
                store_data(extracted)
                send_email(message="Hey, new event was found!")
                connection.close()
