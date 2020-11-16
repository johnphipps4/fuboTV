import requests
import itertools
from selenium import webdriver


# see if we can inherit from webdriver or something
class BrowserSession():
    def __init__(self):

        def _options():
            fireFoxOptions = webdriver.FirefoxOptions()
            fireFoxOptions.add_argument('--headless')
            return fireFoxOptions

        self.options = _options()
        self.drive = webdriver.Firefox(firefox_options = self.options)

    def get_cookie_by_name(self, cookie_name: str):
        cookie_value: str
        for cookie in self.drive.get_cookies():
            if cookie['name'] == cookie_name:
                cookie_value = cookie.get('value', 'Cookie Not Found')
        return cookie_value

class FuboTV():
    URL = 'https://fubo.tv/welcome'
    def __init__(self):
        session = BrowserSession()
        session.drive.implicitly_wait(2)

        # send a browser request to capture cookies
        session.drive.get('https://fubo.tv/welcome')

        self._device_id = session.get_cookie_by_name('ftvOption%3AuniqueId')

        self.headers = {'x-device-id': self._device_id}

    @classmethod
    def from_device_id(cls, device_id):

        pass

    def signin(self, username, password):
        payload = {'email': username, 'password': password}
        response = requests.put('https://api.fubo.tv/signin', headers = self.headers,
                                data = payload, timeout = 2)
        # do error handling for signin request
        # you get a bearer token return it with a token

    def search(self, content):
        pass




if __name__ == "__main__":
    print("1")
