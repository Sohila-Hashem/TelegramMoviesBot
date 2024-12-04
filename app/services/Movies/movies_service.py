import random
from abc import ABC, abstractmethod
from app.services.Movies.movie_api_service import IMovieAPIService

class MovieCategoryMap:
    def __init__(self) -> None:
        raise NotImplementedError
    
    _supported_movie_categories_map = {
        "action": 28,
        "adventure": 12,
        "animation": 16,
        "comedy": 35,
        "crime": 80,
        "documentary": 99,
        "drama": 18,
        "family": 10751,
        "fantasy": 14,
        "history": 36,
        "horror": 27,
        "music": 10402,
        "mystery": 9648,
        "romance": 10749,
        "sciencefiction": 878,
        "tvmovie": 10770,
        "thriller": 53,
        "war": 10752,
        "western": 37,
    }
    
    @staticmethod
    def get_supported_categories() -> list:
        return MovieCategoryMap._supported_movie_categories_map.keys()
    
    @staticmethod
    def get_category_id(category: str) -> int:
        if category not in MovieCategoryMap._supported_movie_categories_map:
            raise ValueError(f"{category} is not a supported movie category")
        return MovieCategoryMap._supported_movie_categories_map[category]

class IMovieService(ABC):
    @abstractmethod
    def __init__(self, API_client: IMovieAPIService) -> None:
        pass

    @abstractmethod
    def get_movies(self, category_id: int, page: int = 1) -> list:
        pass
    
    @abstractmethod
    def get_page_count(self, category_id: int) -> int:
        pass
    
    @abstractmethod
    def get_random_movie(self, movies_list: list) -> list:
        pass
    

# TODO: Make this a singleton
class MovieService(IMovieService):
    def __init__(self, API_client: IMovieAPIService):
        self.API_client:IMovieAPIService = API_client
        
    def get_movies(self, category_id: int, page: int  = 1) -> list:
        movies =  self.API_client.get_movies(category_id, page)
        if movies and movies['results']:
            return movies["results"]
        return None
    
    def get_page_count(self, category_id: int) -> list:
        movies = self.API_client.get_movies(category_id)
        if movies:
            return movies['total_pages']
        return None
    
    def get_random_movie(self, movies_list: list) -> list:
        random_movie_num = random.randint(0, len(movies_list) - 1)
        return movies_list[random_movie_num]
    
