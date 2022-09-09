# -------------------------------------------

import time

from car import Car

# -------------------------------------------


class World:

    # -------------------------------------------

    def __init__(self):

        # Global time in seconds
        self.t = 0.0

        # Time step in seconds
        self.dt = 0.1

        # Simulation flag
        self.running = True

        # Create a car instance
        self.car = Car()

    # -------------------------------------------

    def bang(self):

        self.running = True

        while self.running:

            self.t = self.t + self.dt

            self.__tick__()

            # Prevent burning the cpu
            time.sleep(0.1)

    # -------------------------------------------

    # Mark internal (aka 'private') functions with '__'
    def __tick__(self):

        # Exit loop when the car has stopped
        if not self.car.step(self.dt):

            self.running = False

    # -------------------------------------------

# -------------------------------------------
