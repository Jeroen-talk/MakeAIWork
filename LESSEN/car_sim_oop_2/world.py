import time as tm
from car import Car


class World:
    def __init__(self):
        self.running = True
        self.t = 0.0
        self.dt = 0.1
        self.carA = Car('Tesla', 1100.0, 800)
        self.carB = Car('BMW', 800.0, 900)

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

            if self.carA.x > 100.0:
                print("\n GO Tesla")

                self.running = False

            if self.carB.x > 100.0:
                print("\n F*ck U Elon")

                self.running = False

            tm.sleep(self.dt)
