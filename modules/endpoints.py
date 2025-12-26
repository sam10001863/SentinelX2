import requests
from concurrent.futures import ThreadPoolExecutor
import random

COMMON_PATHS = [
    "admin", "login", "dashboard", "panel", "cpanel",
    "config", "backup", "uploads", "api", "api/v1",
    "robots.txt", "sitemap.xml"
]

DEEP_PATHS = [
    ".env", ".git", ".git/config", ".git/HEAD",
    "config.php", "wp-config.php",
    "test", "dev", "staging", "old", "backup.zip"
]

USER_AGENTS = [
    "Mozilla/5.0",
    "curl/7.81.0",
    "Mozilla/5.0 (X11; Linux x86_64)"
]

def fetch_path(target, path):
    try:
        url = f"http://{target}/{path}"
        headers = {"User-Agent": random.choice(USER_AGENTS)}
        r = requests.get(url, timeout=4, headers=headers)
        if r.status_code in [200, 301, 302, 401, 403]:
            return {
                "path": path,
                "status": r.status_code,
                "length": len(r.text)
            }
    except:
        pass
    return None

def scan_endpoints(target, deep=False):
    paths = COMMON_PATHS + (DEEP_PATHS if deep else [])
    results = []

    with ThreadPoolExecutor(max_workers=10) as exe:
        futures = [exe.submit(fetch_path, target, p) for p in paths]
        for f in futures:
            res = f.result()
            if res:
                results.append(res)

    return results
