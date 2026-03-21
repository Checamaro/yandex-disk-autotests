def to_curl(request):

    command = f"curl -X {request.method} '{request.url}'"

    for k, v in request.headers.items():
        command += f" -H '{k}: {v}'"

    return command