import os
import requests
from typing import Optional, Dict, Any, List

class APIClient:
    def __init__(self, base_url: str = "https://api.example.com", api_key: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        
        self.api_key = api_key or os.getenv("API_KEY")
        if self.api_key:
            self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})

    def _request(self, method: str, endpoint: str, **kwargs) -> Any:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
            raise
        except Exception as e:
            print(f"Request Error: {e}")
            raise

    # TODO: Add dynamic methods here
    def get_resource(self, resource_id: str) -> Dict[str, Any]:
        """Example GET request"""
        return self._request("GET", f"resources/{resource_id}")

    def create_resource(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Example POST request"""
        return self._request("POST", "resources", json=data)
