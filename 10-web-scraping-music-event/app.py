from event import Event
from _email import Email
from database import Data

endpoint = 'http://programmer100.pythonanywhere.com/tours/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

event = Event(headers=headers, url=endpoint)
email = Email()
database = Data()
