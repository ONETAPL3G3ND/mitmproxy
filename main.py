from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    flow.request.headers["User-Agent"] = "MyCustomUserAgent/1.0"

def response(flow: http.HTTPFlow) -> None:
    if "example.com" in flow.request.pretty_host:
        flow.response.text = flow.response.text.replace("Example Domain", "Modified Domain")
