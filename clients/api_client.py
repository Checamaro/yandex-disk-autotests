import requests

from config import BASE_URL, TOKEN, TIMEOUT
from clients.event_hooks import log_request, log_response


class ApiClient:

    def __init__(self):
        self.session = requests.Session()

        self.session.headers.update({

            "Authorization": f"OAuth {TOKEN}",

            "Accept": "application/json"

        })

        self.session.hooks = {"response": [log_response]}

    def get(self, url, params=None):
        r = self.session.get(
            BASE_URL + url,
            params=params,
            timeout=TIMEOUT
        )

        log_request(r.request)

        return r

    def post(self, url, params=None):
        r = self.session.post(
            BASE_URL + url,
            params=params,
            timeout=TIMEOUT
        )

        log_request(r.request)

        return r

    def put(self, url, params=None):
        r = self.session.put(
            BASE_URL + url,
            params=params,
            timeout=TIMEOUT
        )

        log_request(r.request)

        return r

    def delete(self, url, params=None):
        r = self.session.delete(
            BASE_URL + url,
            params=params,
            timeout=TIMEOUT
        )

        log_request(r.request)

        return r
