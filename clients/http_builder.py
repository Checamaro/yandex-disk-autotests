import requests

from config import BASE_URL, TOKEN, TIMEOUT
from clients.event_hooks import log_request, log_response


def get_http_client() -> requests.Session:
    session = requests.Session()

    session.headers.update({
        "Authorization": f"OAuth {TOKEN}",
        "Accept": "application/json"
    })

    session.base_url = BASE_URL
    session.timeout = TIMEOUT

    session.hooks = {
        "response": [log_response]
    }

    return session
