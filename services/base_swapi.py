import requests


class BaseSwApiClient:
    """Base class for SW API clients"""

    BASE_URL = "https://swapi.dev/api"

    def __init__(self):
        self.client = requests.Session()

    def close(self):
        """Close HTTP session"""
        self.client.close()
