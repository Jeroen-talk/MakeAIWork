#-------------------------------------------

import time

#-------------------------------------------

class World:

    #-------------------------------------------

    def __init__(self):

        # Global time in seconds
        self.t = 0.0

        # Time step in seconds
        self.dt = 0.1

        # Simulation flag
        self.running = True

        # Reserve a track spot
        self.track = None

    #-------------------------------------------

    def addTrack(self, track):

        self.track = track


    #-------------------------------------------

    def bang(self):

        self.running = True
        
        while self.running:
            
            self.t = self.t + self.dt

            self.__tick__()

            # Prevent burning the cpu
            time.sleep(0.1)

    #-------------------------------------------
    
    # Mark internal (aka 'private') functions with '__'
    def __tick__(self):

        if not self.track.step(self.t, self.dt):

            self.track.saveResults()

            self.running = False

    #-------------------------------------------

#-------------------------------------------