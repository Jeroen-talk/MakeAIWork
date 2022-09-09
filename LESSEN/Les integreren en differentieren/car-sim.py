#-------------------------------------------

import time

#-------------------------------------------

# Global time in seconds
t = 0.0

# Time step in seconds
dt = 0.1

#-------------------------------------------

# Car's mass in kilogram
m = 600.0

# Car's thrust in Newton
F = 800.0

# Car's start speed in m/s
v = 0.0

# Car's displacement in meters
x = 0.0

#-------------------------------------------

# Simulation flag
running = True

#-------------------------------------------

while running:

    t += dt

    print("t: ", t)

    a = F / m

    dv = a * dt
    v = v + dv

    print("v: ", v)

    dx = v * dt
    x = x + dx

    print("x: ", x)

    # Prevent burning the cpu
    time.sleep(0.1)

    if x > 100.0:
        
        running = False # or use 'break' to break out of the loop

#-------------------------------------------

print("Duration: ", t, " seconds")

#-------------------------------------------