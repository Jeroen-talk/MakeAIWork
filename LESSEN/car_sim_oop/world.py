import time as tm
from car import Car


class World:
    # Constructor
    def __init__(self):
        self.t = 0.0
        self.dt = 0.1

        self.running = True

    def
    addCar(self, car):
        self.cars.append(car)

    def bang(self):
        while self.running:
            self.t += self.dt
            self.car.move(self.dt)
            if self.car.x > 100:
                self.running = False
            print("Time: ", self.t)
            tm.sleep(self.dt)

    def stop(self):
        self.running = False


BMW = Car("BMW", 800, 700)
Tesla = Car("Tesla", 900, 600)
