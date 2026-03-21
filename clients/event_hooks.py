import allure
import logging, re
from tools.http.curl import to_curl
from tools.logger import get_logger

logger = get_logger()


def mask_token(text: str) -> str:
    return re.sub(r'OAuth\s+\w+', 'OAuth [MASKED]', text)


def log_request(request):
    logger.info(f"{request.method} {request.url}")

    curl = to_curl(request)
    curl = mask_token(curl)

    allure.attach(
        curl,
        name="curl",
        attachment_type=allure.attachment_type.TEXT
    )


def log_response(response, *args, **kwargs):
    import json
    status_line = f"[{response.status_code}] {response.request.method} {response.url}"
    print(mask_token(status_line))  # <-- маскируем токен в логах

    try:
        body = json.dumps(response.json(), indent=2, ensure_ascii=False)
        print(mask_token(body))
    except Exception:
        print(mask_token(response.text))
    return response


logging.basicConfig(level=logging.INFO)