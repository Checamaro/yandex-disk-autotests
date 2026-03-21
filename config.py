from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = "https://cloud-api.yandex.net"
TOKEN = os.getenv("YANDEX_TOKEN")
TIMEOUT = 10