from __future__ import annotations
from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
    movie_show_time: str,
    movie_id: int,
    cinema_hall_id: int
) -> None:
    movie = Movie.objects.get(pk=movie_id)
    cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: str = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> None | str:
    try:
        movie_session = MovieSession.objects.get(pk=session_id)
    except MovieSession.DoesNotExist:
        return "Session with this id doesn't exist"

    if show_time:
        movie_session.show_time = show_time

    if movie_id:
        try:
            movie = Movie.objects.get(pk=movie_id)
            movie_session.movie = movie
        except Movie.DoesNotExist:
            return "Session with this id doesn't exist"

    if cinema_hall_id:
        try:
            cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)
            movie_session.cinema_hall = cinema_hall
        except CinemaHall.DoesNotExist:
            return "Session with this id doesn't exist"

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None | str:
    try:
        movie_session = MovieSession.objects.get(pk=session_id)
        movie_session.delete()
    except MovieSession.DoesNotExist:
        return "Session with this id doesn't exist"