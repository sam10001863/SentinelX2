from core.scanner import run_scan
from core.risk import calculate_risk
from reports.text_report import generate_text
from reports.html_report import generate_html

def run(target, deep=False):
    print("Starting full scan...")
    data = run_scan(target, deep)
    risk = calculate_risk(data)

    generate_text(target, data, risk)
    generate_html(target, data, risk)
