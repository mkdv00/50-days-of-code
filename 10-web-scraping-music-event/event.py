import requests
import selectorlib


class Event:

    def __init__(self, headers, url):
        self.headers = headers
        self.url = url
        self.source = None

    def scrape(self):
        """Scrape the page source from the url"""
        response = requests.get(self.url, headers=self.headers)
        self.source = response.text
        return self

    def extract(self):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(self.source)["tours"]
        return value
