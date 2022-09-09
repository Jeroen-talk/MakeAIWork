#-------------------------------------------

class Track:

    #-------------------------------------------

    def __init__(self, distance):
        
        self.distance = distance

        # List of cars
        self.cars = []

    #-------------------------------------------

    def addCar(self, car):

        self.cars.append(car)

    #-------------------------------------------

    def step(self, dt):

        for car in self.cars:

            x, v = car.step(dt)
            
            # Stop simulation when the car has reached end of track
            if x > self.distance:

                print("We have a winner: ", car.name)

                return False
        
        return True

    #-------------------------------------------

#-------------------------------------------