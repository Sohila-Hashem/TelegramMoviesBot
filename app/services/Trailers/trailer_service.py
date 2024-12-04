from abc import ABC, abstractmethod
from app.services.Trailers.trailer_api_service import ITrailerAPIService

class ITrailerService(ABC):
    @abstractmethod
    def __init__(self, API_client: ITrailerAPIService) -> None:
        pass

    @abstractmethod
    def get_movie_trailers(self, movie_id: int) -> list:
        pass

    @abstractmethod
    def filter_trailers(self, trailers: list, site: str = "YouTube") -> list:
        pass

class TrailerService():
    def __init__(self, API_client: ITrailerAPIService) -> None:
        self.API_client:ITrailerAPIService = API_client

    def get_movie_trailers(self, movie_id: int) -> list:
        return self.API_client.get_movie_trailers(movie_id)

    def filter_trailers(self, trailers: list, site: str = "YouTube") -> list:
        if trailers and len(trailers):
            return list(filter(lambda x: x["type"] == "Trailer" and x["site"] == site and x['official'] == True, trailers))
        return None