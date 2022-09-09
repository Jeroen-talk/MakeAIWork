#-------------------------------------------

from world import World

from track import Track

from car import Car

#-------------------------------------------

# Create new world instance
world = World()

# Create new track instance
track = Track(100)

# Create a Tesla
tesla = Car("Tesla", 600, 800)

# Creat a BMW
bmw = Car("BMW", 1200, 900)

track.addCar(tesla)
track.addCar(bmw)

# Add track to world
world.addTrack(track)

# Start the simulation
world.bang()

#-------------------------------------------