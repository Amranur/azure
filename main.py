from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>FastAPI on Azure</title>
        </head>
        <body>
            <h1>FastAPI is successfully running on Azure!</h1>
        </body>
    </html>
    """
