import requests
from dotenv import load_dotenv
import os
import json
import smtplib, ssl

load_dotenv()


def get_last_article():
    username = 'maxim.cudaew@gmail.com'

    api_key = os.getenv('API_KEY')
    api_url = os.getenv('API_URL')
    url = f"{api_url}?q=tesla&sortBy=publishedAt&apiKey={api_key}"

    response = requests.get(url)
    content = response.json()['articles'][:10]

    msgs = []
    for article in content:
        msg = f"Subject: {article['title']}\n" \
              f"From: {article}\n" \
              f"{article['description']}\n" \
              f"Url: {article['url']}\n" \
              f"Image: {article['urlToImage']}"
        msgs.append(msg)

    return msgs


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'maxim.cudaew@gmail.com'
    password = os.getenv('PASSWORD')

    print(f"Username: {username}, Password: {password}")

    receiver = username
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as connection:
        connection.login(username, password)
        connection.sendmail(username, receiver, message.encode('utf-8'))


if __name__ == '__main__':
    last_ten_articles = get_last_article()

    for article in last_ten_articles:
        send_email(article)
