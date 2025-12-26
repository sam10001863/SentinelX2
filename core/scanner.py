from modules.ports import scan_ports
from modules.headers import scan_headers
from modules.endpoints import scan_endpoints
from core.https import check_https

def run_scan(target, deep=False):
    results = {}

    print("[*] Scanning ports...")
    results['ports'] = scan_ports(target)

    print("[*] Scanning headers...")
    results['headers'] = scan_headers(target)

    print("[*] Scanning endpoints...")
    results['endpoints'] = scan_endpoints(target, deep)

    print("[*] Checking HTTPS...")
    results['https'] = check_https(target)

    return results
