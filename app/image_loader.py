
import requests
from PIL import Image
from io import BytesIO

def load_dashboard_image(snapshot_url):
    r = requests.get(snapshot_url)
    r.raise_for_status()
    return Image.open(BytesIO(r.content))

