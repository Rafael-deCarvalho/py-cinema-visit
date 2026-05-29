from people import customer


class CinemaHall:

    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number
    

    def movie_session(self, movie_name: str, customers: list[Customer], cleaning_staff: Cleaner) -> None:
        
        print (f"{movie_name} started in hall number {self.hall_number}")

        for customer in customers:
            Customer.watch_movie(customer)

        print(f"{movie_name} ended")
        Cleaner.clean_hall(cleaning_staff)