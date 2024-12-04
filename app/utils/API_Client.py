from abc import ABC, abstractmethod
from requests_toolbelt import sessions

class IAPIClient(ABC):
    @abstractmethod
    def __init__(self, base_url: str, params: object, headers: object) -> None:
        pass

    def get(self, url: str, params: object = None) -> object:
        pass

class APIClient:
    def __init__(self, base_url, params, headers) -> None:
        self.client = sessions.BaseUrlSession(base_url)
        self.client.headers = headers
        self.client.params = params

    def get(self, url, params=None):
        return self.client.get(url, params=params).json()
