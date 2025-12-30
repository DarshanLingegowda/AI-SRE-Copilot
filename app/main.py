from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="AI SRE Copilot")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def landing():
    return Path("app/static/index.html").read_text()

@app.post("/analyze-incident-multimodal")
async def analyze_multimodal(request: Request):
    payload = await request.json()
    return {
        "analysis": {
            "root_cause": "High token usage caused increased latency",
            "impact": "LLM responses exceeded SLA during peak traffic",
            "fix": "Reduce max tokens and enable rate limiting"
        },
        "input": payload
    }
