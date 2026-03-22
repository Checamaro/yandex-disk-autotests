def to_curl(request):
    command = f"curl -X {request.method} '{request.url}'"

    for key, value in request.headers.items():
        command += f" -H '{key}: {value}'"
    return command
