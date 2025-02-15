import glob
import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse

app = FastAPI()

LOGS_DIR = os.path.join(os.path.abspath(os.curdir), "logs")


@app.get("/", response_class=JSONResponse)
def read_root():
    return {"app_name": "API Rest"}


@app.get("/logs/", response_class=HTMLResponse)
def logs():
    files = glob.glob(f"{LOGS_DIR}/*.log")

    html_content = f"""
    <html>
        <body>
            {"<br>".join({ f"<a href={os.path.basename(item)}>{item}</a>" for item in files }) }
        </body>
    </html>
    """
    return html_content


@app.get("/logs/{file_path}", response_class=PlainTextResponse)
def logs_item(file_path: str):
    with open(os.path.join(LOGS_DIR, file_path)) as f:
        return f.read()
