import random



class Passenger:

    BOARDING_CLASSES = {
        "business": "b",
        "economy": "e",
        "basic_econ": "be",
        "first_class": "fc"
    }

    def __init__(self, boarding_class, seat):
        self.assign_name()
        self.boarding_class = boarding_class
        self.seat = seat

    def assign_name(self):
        with open('assets/names.txt') as f:
            names = f.readlines()
        self.name = random.choice(names).strip()

    def __str__(self) -> str:
        return self.name + ":" + self.boarding_class
    
    def __repr__(self) -> str:
        return self.name + ":" + self.boarding_class