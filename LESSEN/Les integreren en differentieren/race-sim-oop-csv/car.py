#-------------------------------------------

import csv

#-------------------------------------------

class Car:

    #-------------------------------------------

    def __init__(self, name, mass, thrust):

        # Car's start speed in m/s
        self.v = 0.0

        # Car's displacement in meters
        self.x = 0.0

        # List of recordings
        self.recording = []
        
        # Cars identifier
        self.name = name

        # Car's mass in kilogram
        self.m = mass

        # Car's thrust in Newton
        self.F = thrust

    #-------------------------------------------

    def step(self, t, dt):

        a = self.F / self.m

        dv = a * dt
        self.v = self.v + dv

        dx = self.v * dt
        self.x = self.x + dx

        self.recording.append([t, self.x, self.v])

        return self.x, self.v

    #-------------------------------------------

    def saveResults(self):

        # Colomn names
        fields = ["time (s)", "position (m)", "speed (m/s)"]

        # Save the recording to disk
        with open(self.name + ".csv", 'w') as f:

            # Using csv.writer method from CSV package
            write = csv.writer(f)
            
            write.writerow(fields)
            write.writerows(self.recording)

    #-------------------------------------------

#-------------------------------------------