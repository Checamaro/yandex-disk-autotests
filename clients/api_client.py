import allure
import requests

from tools.allure.attachments import attach_request, attach_response
from clients.http_builder import get_http_client
from clients.event_hooks import log_request


class ApiClient:

    def __init__(self, session: requests.Session | None = None):
        self.session = session or get_http_client()

    def _request(self, method: str, url: str, **kwargs):
        full_url = self.session.base_url + url

        with allure.step(f"{method.upper()} {url}"):
            r = self.session.request(
                method,
                full_url,
                timeout=self.session.timeout,
                **kwargs
            )

            log_request(r.request)

            attach_request(r.request)
            attach_response(r)

            return r

    def get(self, url, **kwargs):
        return self._request("GET", url, **kwargs)

    def post(self, url, **kwargs):
        return self._request("POST", url, **kwargs)

    def put(self, url, **kwargs):
        return self._request("PUT", url, **kwargs)

    def patch(self, url, **kwargs):
        return self._request("PATCH", url, **kwargs)

    def delete(self, url, **kwargs):
        return self._request("DELETE", url, **kwargs)
