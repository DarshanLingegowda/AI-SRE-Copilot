
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

vertexai.init(project="YOUR_GCP_PROJECT_ID", location="us-central1")
model = GenerativeModel("gemini-1.5-pro")

def analyze_incident_multimodal(incident_text, metrics_json, logs_text, dashboard_image):
    prompt = f"""You are an AI SRE Copilot.

Incident:
{incident_text}

Metrics:
{metrics_json}

Logs:
{logs_text}

Tasks:
- Identify root cause
- Assess impact
- Recommend fixes
"""

    response = model.generate_content(
        contents=[prompt, Part.from_image(dashboard_image)],
        generation_config={"temperature": 0.2}
    )
    return response.text

