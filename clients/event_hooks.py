import allure
import logging, re
from tools.http.curl import to_curl
from tools.logger import get_logger
import json

logger = get_logger()


def mask_token(text: str) -> str:
    return re.sub(r'OAuth\s+[^\s\'"]+', 'OAuth [MASKED]', text)


def log_request(request):
    if 'Authorization' in request.headers:
        request.headers['Authorization'] = 'OAuth [MASKED]'

    curl = to_curl(request)
    curl = mask_token(curl)

    logger.info(curl)
    allure.attach(
        curl,
        name="curl",
        attachment_type=allure.attachment_type.TEXT
    )


def log_response(response, *args, **kwargs):
    logger.info(f"Response status: {response.status_code}")
    logger.info(f"Response url: {response.url}")

    try:
        body = response.json()
        logger.info(f"Response body: {json.dumps(body, indent=2, ensure_ascii=False)}")
    except Exception:
        logger.info(f"Response body: {response.text}")

    return response


logging.basicConfig(level=logging.INFO)
