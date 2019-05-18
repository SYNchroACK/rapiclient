from urllib.parse import urljoin
import requests
import json


class Response(object):

    def __init__(self, details):
        for key, value in details.items():
            setattr(self, key, value)

    def __str__(self):
        return "Ok: %s / Status: %s / Data: %s" % (self.ok, self.status, self.data)


def process_response(resp):
    response = Response({
        "ok": False,
        "status": resp.status_code,
        "data": parse_content(resp.content)
    })

    if 400 <= resp.status_code <= 499:
        return response

    elif 500 <= resp.status_code <= 599:
        return response

    response.ok = True
    return response

def parse_content(content):
    if not content:
        return None

    if type(content) != bytes:
        return json.loads(content)

    try:
        encoding = requests.utils.guess_json_utf(content)
        return json.loads(content.decode(encoding))
    except Exception:
        return content

def join_url(paths):
    url = ""
    for path in paths:
        url = urljoin(url, path)
    return url