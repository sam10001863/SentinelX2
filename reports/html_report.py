def generate_html(target, data, risk):
    filename = "reports/report.html"

    html = f"""
    <html>
    <head>
        <title>SentinelX Report</title>
        <style>
            body {{ font-family: Arial; background: #111; color: #eee; padding: 20px; }}
            h1 {{ color: #00ffcc; }}
            .box {{ border: 1px solid #444; padding: 10px; margin: 10px 0; }}
        </style>
    </head>
    <body>
        <h1>SentinelX Scan Report</h1>

        <p><b>Target:</b> {target}</p>
        <p><b>Risk Level:</b> {risk}</p>

        <div class="box">
            <h3>Open Ports</h3>
            <pre>{data['ports']}</pre>
        </div>

        <div class="box">
            <h3>Security Headers</h3>
            <pre>{data['headers']}</pre>
        </div>

        <div class="box">
            <h3>Endpoints Found</h3>
            <pre>{data['endpoints']}</pre>
        </div>

    </body>
    </html>
    """

    with open(filename, "w") as f:
        f.write(html)

    print(f"[+] HTML report saved to {filename}")
