import requests
import json

class AdafruitIO:
    def __init__(self, adafruit_io_key, username):
        self.adafruit_io_key = adafruit_io_key
        self.username = username

    @property
    def url(self):
        return "https://io.adafruit.com/api/v2/" + self.username

    @property
    def headers(self):
        return {'X-AIO-Key': self.adafruit_io_key}

    def emit(self, feed_key, value):
        data = { "value" : value }
        url = self.url + "/feeds/" + feed_key + "/data/"
        try:
            r = requests.post(url, headers=self.headers,
                              json=data)
        finally:
            r.close()

    def read(self, feed_key):
        url = self.url + "/feeds/" + feed_key + "/data/last?include=value"
        try:
            r = requests.get(url, headers=self.headers)
            data = r.json()
        finally:
            r.close()
        return data
