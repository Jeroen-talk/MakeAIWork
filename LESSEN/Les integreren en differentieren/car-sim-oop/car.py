#-------------------------------------------

class Car:

    # Car's mass in kilogram
    m = 600.0

    # Car's thrust in Newton
    F = 800.0

    # Car's start speed in m/s
    v = 0.0

    # Car's displacement in meters
    x = 0.0

    #-------------------------------------------

    def step(self, dt):

        a = self.F / self.m

        dv = a * dt
        self.v = self.v + dv

        print("v: ", self.v)

        dx = self.v * dt
        self.x = self.x + dx

        print("x: ", self.x)

        if self.x < 100.0:

            return True
        
        else:

            return False

    #-------------------------------------------

#-------------------------------------------