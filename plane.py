
import queue
import random
from seat import Seat 
from passenger import Passenger 

# BOARDING_CLASSES = {
#     "business": "b",
#     "economy": "e",
#     "basic_econ": "be",
#     "first_class": "fc"
# }

class Plane:
    def __init__(self):
        #Important information for the plane
        self.ROWS = 16
        self.COLUMNS = 6
        self.TOTAL_SEATS = self.ROWS * self.COLUMNS #typically 96
        self.row_letters = "abcdef"
       
        #Keeping track of our passengers
        self.passengers = [self.ROWS * self.COLUMNS]
        self.passenger_line = queue.Queue()

        #Define open seats
        self.seats = [[Seat(str(i) + ":" + self.row_letters[j]) for j in range(self.COLUMNS)] for i in range(self.ROWS)]

    def create_passengers(self):
        for i in range(self.ROWS):
            for j in range(self.COLUMNS):
                one_fourth = self.ROWS/4
                if i <= one_fourth:
                    self.passengers.append(Passenger(Passenger.BOARDING_CLASSES["first_class"],self.seats[i][j]))
                elif i > one_fourth and i <= one_fourth*2:
                    self.passengers.append(Passenger(Passenger.BOARDING_CLASSES["business"],self.seats[i][j]))
                elif i > one_fourth*2 and i<=one_fourth*3:
                    self.passengers.append(Passenger(Passenger.BOARDING_CLASSES["economy"],self.seats[i][j]))
                elif i>one_fourth*3:
                    self.passengers.append(Passenger(Passenger.BOARDING_CLASSES["basic_econ"],self.seats[i][j]))

    def fill_queue_standard(self):
        for i in range(self.passengers):
            pass

    def get_seats(self):
        return self.seats

def main():
    new_plane = Plane()
    print("\nSeats:\n")
    print(new_plane.get_seats())
    new_plane.create_passengers()
    print("\nPassengers:\n")
    print(new_plane.passengers)
    print("\n")





main()