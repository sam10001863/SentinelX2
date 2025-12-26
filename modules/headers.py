import requests

SEC_HEADERS = [
    "X-Frame-Options",
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options"
]

def scan_headers(target):
    result = {}
    try:
        r = requests.get(f"http://{target}", timeout=5)
        for h in SEC_HEADERS:
            result[h] = "OK" if h in r.headers else "MISSING"
    except:
        for h in SEC_HEADERS:
            result[h] = "MISSING"
    return result
