
from fastapi import FastAPI
from app.gemini import analyze_incident_multimodal
from app.datadog_snapshot import get_dashboard_snapshot
from app.image_loader import load_dashboard_image

app = FastAPI(title="AI SRE Copilot")

@app.get("/")
def home():
    return {"project": "AI SRE Copilot", "status": "running"}

@app.post("/analyze-incident-multimodal")
async def analyze_multimodal():
    snapshot_url = get_dashboard_snapshot("DASHBOARD_ID")
    image = load_dashboard_image(snapshot_url)

    analysis = analyze_incident_multimodal(
        incident_text="Latency spike detected",
        metrics_json="{ latency: 4200, error_rate: 0.08 }",
        logs_text="Timeout errors detected",
        dashboard_image=image
    )
    return {"analysis": analysis}

