from flask import Flask, request, Response
import base64
import logging
import os
import time

app = Flask(__name__)

# Logging
logging_level = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL,
}
LEVEL: str = os.getenv("LOG_LEVEL", "info")
app.logger.setLevel(logging_level[LEVEL])


def response_text(result: str, report_file: str) -> str:
    return f"""Content-Type: text/plain
#!ipxe
echo Result {result} saved in {report_file} on server.
echo Press enter to continue
read dummy
exit
"""


def write_report(content: str, filename: str) -> None:
    with open(filename, "w") as fh:
        report = content
        fh.write(report)


@app.route("/memtest_report", methods=["GET", "POST"])
def memtest_report():
    result = request.args.get("result", "")
    vram = base64.b64decode(request.args.get("vram", "").encode()).decode()
    mac = request.args.get("mac", "")
    uuid = request.args.get("uuid", "")
    hostname = request.args.get("hostname", "")
    product = request.args.get("product", "")
    manufacturer = request.args.get("manufacturer", "")
    asset = request.args.get("asset", "")
    serial = request.args.get("serial", "")
    board_serial = request.args.get("board-serial", "")

    report_file = f"reports/memtest-report-{uuid}-{int(time.time())}.txt"
    content = f"""Memtest result: {result}
MAC: {mac} {f'({hostname})' if hostname else ""}
UUID: {uuid}
Product: {product} ({manufacturer})
Serial: {serial} (board: {board_serial})
Asset: {asset}
{vram}
"""
    write_report(content, report_file)

    app.logger.info(f"Result {result} saved in {report_file} on server for UUID {uuid}")

    return Response(response_text(result, report_file), 200, content_type="text/plain")


# if __name__ == "__main__":
#     app.logger.info("Starting memtest_report")
#     app.run(host="0.0.0.0")
