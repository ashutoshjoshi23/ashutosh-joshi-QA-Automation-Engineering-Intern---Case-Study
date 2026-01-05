import requests

class APIClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def post(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=data, headers=self.headers)
        return response

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers)
        return response
