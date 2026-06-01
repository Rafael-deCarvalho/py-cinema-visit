from app.cinema import bar, hall
from app.people import customer, cinema_staff


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:

    for customer in customers:
        sell_product(customer["food"], customer["name"])

    movie_session(movie, customers, cleaner)