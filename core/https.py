import requests

def check_https(target):
    try:
        r = requests.get(f"https://{target}", timeout=5)
        return {"enabled": True, "status": r.status_code}
    except:
        return {"enabled": False}
