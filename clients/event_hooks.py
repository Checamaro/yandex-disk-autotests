import allure

from tools.http.curl import to_curl
from tools.logger import get_logger

logger = get_logger()


def log_request(request):
    logger.info(f"{request.method} {request.url}")

    curl = to_curl(request)

    allure.attach(
        curl,
        name="curl",
        attachment_type=allure.attachment_type.TEXT
    )


def log_response(response, *args, **kwargs):
    """Логирование HTTP-ответа без ошибок с kwargs от requests"""
    import json
    print(f"[{response.status_code}] {response.request.method} {response.url}")
    try:
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except Exception:
        print(response.text)
    return response
