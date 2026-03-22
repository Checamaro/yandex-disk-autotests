import json
import allure


def attach_request(request):
    body = request.body
    if isinstance(body, bytes):
        body = body.decode()

    data = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "body": body
    }

    allure.attach(
        json.dumps(data, indent=2, ensure_ascii=False),
        name="request",
        attachment_type=allure.attachment_type.JSON
    )


def attach_response(response):
    try:
        body = json.dumps(response.json(), indent=2, ensure_ascii=False)
    except Exception:
        body = response.text

    data = {
        "status_code": response.status_code,
        "body": body
    }

    allure.attach(
        json.dumps(data, indent=2, ensure_ascii=False),
        name="response",
        attachment_type=allure.attachment_type.JSON
    )
