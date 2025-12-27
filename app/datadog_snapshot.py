
import requests, os

DD_API_KEY = os.getenv("DD_API_KEY")
DD_APP_KEY = os.getenv("DD_APP_KEY")

def get_dashboard_snapshot(dashboard_id: str):
    url = "https://api.datadoghq.com/api/v1/graph/snapshot"
    payload = {
        "metric_query": "avg:llm.response.latency_ms{*}",
        "start": "now-15m",
        "end": "now"
    }
    headers = {
        "DD-API-KEY": DD_API_KEY,
        "DD-APPLICATION-KEY": DD_APP_KEY
    }
    r = requests.post(url, headers=headers, json=payload)
    r.raise_for_status()
    return r.json()["snapshot_url"]

