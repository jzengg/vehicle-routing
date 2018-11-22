class Car:
    
    def __init__(self):
        self.passengers = []

    def pickup(self, passenger):
        self.passengers.append(passenger)

    def dropoff(self, passenger):
        self.passengers.remove(passenger)
