import time as tm
from car import Car


class World:
    # Constructor
    def __init__(self):
        self.t = 0.0
        self.dt = 0.1
        self.carA = Car("BMW", 600.0, 800.0)
        self.carB = Car("Tesla", 800.0, 800.0)

    def bang(self):
        while self.running:
            self.t += self.dt

            self.carA.move(self.dt)
            self.carB.move(self.dt)

            if self.carA.x > 100:
                self.running = False
            if self.carB.x > 100:
                self.running = False

            print("Time: ", self.t)
            tm.sleep(self.dt)
