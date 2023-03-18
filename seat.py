class Seat:
    def __init__(self, seat_code):
        self.seat_code = seat_code
        self.current_passenger = None
        self.seat_full = False

    def fill_seat(self, person):
        self.current_passenger = person
        self.seat_full = True

    def __str__(self) -> str:
        return self.seat_code
    
    def __repr__(self) -> str:
        return self.seat_code
