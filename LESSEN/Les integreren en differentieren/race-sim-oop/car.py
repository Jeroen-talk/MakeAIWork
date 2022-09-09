#-------------------------------------------

class Car:

    #-------------------------------------------

    def __init__(self, name, mass, thrust):

        # Car's start speed in m/s
        self.v = 0.0

        # Car's displacement in meters
        self.x = 0.0
        
        # Cars identifier
        self.name = name

        # Car's mass in kilogram
        self.m = mass

        # Car's thrust in Newton
        self.F = thrust

    #-------------------------------------------

    def step(self, dt):

        a = self.F / self.m

        dv = a * dt
        self.v = self.v + dv

        dx = self.v * dt
        self.x = self.x + dx

        return self.x, self.v

    #-------------------------------------------

#-------------------------------------------