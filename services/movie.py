from django.db.models import Q, QuerySet

from db.models import Movie, Genre, Actor


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    movies = Movie.objects.all()

    if genres_ids and actors_ids:
        movies = movies.filter(
            Q(genres__in=genres_ids) & Q(actors__in=actors_ids)
        )
    elif genres_ids:
        movies = movies.filter(genres__in=genres_ids)
    elif actors_ids:
        movies = movies.filter(actors__in=actors_ids)

    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list = None,
    actors_ids: list = None
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        new_movie.genres.add(*genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        new_movie.actors.add(*actors)

    return new_movie