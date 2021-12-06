import requests
import uuid

QR_ODE_GEN_BASE_ENDPOINT = "https://api.qrserver.com/v1/create-qr-code/?size=150x150"


class QrCodeImg:
    def __init__(self, data):
        self.response = requests.get(QR_ODE_GEN_BASE_ENDPOINT, params={"data": data})
        self.file_name = f"{uuid.uuid4()}.png"
        self.file_path = f"static/temp/{self.file_name}"
        with open(self.file_path, "wb") as file:
            file.write(self.response.content)