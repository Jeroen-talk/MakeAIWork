
class Car:

    # The Constructor
    def __init__(self, name, F, m):

        self.name = name

        self.F = F
        self.m = m

        self.x = 0.0
        self.v = 0.0

    def move(self, dt):

        a = self.F / self.m

        dv = a * dt
        self.v = self.v + dv

        print("v: ", self.v)

        dx = self.v * dt
        self.x = self.x + dx

        print("x: ", self.x)
