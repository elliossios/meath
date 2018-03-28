import requests

class GeoApi:
    def __init__(self, url, *args, **kwargs):
        self.url = url

    def get_location(self):
        r = requests.get(self.url)
        return r.json()