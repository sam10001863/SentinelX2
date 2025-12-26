from core.version import VERSION

def generate_text(target, data, risk):
    print("\n========== SENTINELX REPORT ==========")
    print(f"Version: {VERSION}")
    print("Target:", target)
    print("Risk Level:", risk)

    print("\n[+] HTTPS")
    print(data["https"])

    print("\n[+] Open Ports")
    print(data["ports"])

    print("\n[+] Security Headers")
    for k, v in data["headers"].items():
        print(f"  {k}: {v}")

    print("\n[+] Endpoints Found")
    for e in data["endpoints"]:
        print(f"  /{e['path']}  -> {e['status']} ({e['length']} bytes)")
