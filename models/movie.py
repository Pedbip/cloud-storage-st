import requests

def get_movies():
    req = requests.get('https://api.potterdb.com/v1/movies')
    if req.status_code == 200:
        return req.json()
    else:
        raise Exception(f"Failed to fetch movies: {req.status_code}")
    
def get_movie_by_id(movie_id):
    req = requests.get(f'https://api.potterdb.com/v1/movies/{movie_id}')
    if req.status_code == 200:
        return req.json()
    else:
        raise Exception(f"Failed to fetch movie with ID {movie_id}: {req.status_code}")