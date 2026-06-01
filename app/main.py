from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:

    for client in customers:
        CinemaBar.sell_product(client["food"], client["name"])

    CinemaHall.movie_session(movie, customers, cleaner)
