from core.engine import run
from utils.banner import show_banner
import sys

def main():
    show_banner()

    if len(sys.argv) < 2:
        print("Usage: python sentinelx2.py <target> [--deep]")
        exit()

    target = sys.argv[1]
    deep = False

    if len(sys.argv) == 3 and sys.argv[2] == "--deep":
        deep = True

    run(target, deep)

if __name__ == "__main__":
    main()
