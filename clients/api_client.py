import requests
import allure

from config import BASE_URL, TOKEN, TIMEOUT
from clients.event_hooks import log_request, log_response
from tools.allure.attachments import (
    attach_request,
    attach_response
)


class ApiClient:

    def __init__(self):
        self.session = requests.Session()

        self.session.headers.update({
            "Authorization": f"OAuth {TOKEN}",
            "Accept": "application/json"
        })

        self.session.hooks = {"response": [log_response]}

    def _request(self, method, url, params=None):
        full_url = BASE_URL + url

        with allure.step(f"{method.upper()} {url}"):
            r = self.session.request(
                method,
                full_url,
                params=params,
                timeout=TIMEOUT
            )

            log_request(r.request)

            attach_request(r.request)
            attach_response(r)

            return r

    def get(self, url, params=None):
        return self._request("GET", url, params)

    def post(self, url, params=None):
        return self._request("POST", url, params)

    def put(self, url, params=None):
        return self._request("PUT", url, params)

    def delete(self, url, params=None):
        return self._request("DELETE", url, params)
