from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_index() -> str:
    # Read the HTML file content
    html_path = Path("C4C_Categoriekiezer.html")
    return html_path.read_text(encoding="utf-8")


def main() -> None:
    # Run the web server
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
