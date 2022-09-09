import time as tm


class World:
    # Constructor
    def __init__(self):
        self.t = 0.0
        self.dt = 0.1

        self.running = True


def bang(self):
    while self.running:
        self.t += self.dt
        print("Time: ", self.t)
        tm.sleep(self.dt)


def stop(self):
    self.running = False
