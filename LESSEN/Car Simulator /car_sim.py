# ----------------------------

from re import M
import time

# ----------------------------

# Global time in second
t = 0.0

# Time step in seconds
dt = 0.1

# ----------------------------

# Car's mass in kilogram
m = 600.0

# Cars thrust in Newton
F = 800.0

# Ca's  start speed m/s
v = 0.0

# Car's displacement in meters
x = 0.0

# ----------------------------

# Simulation flag finnish
running = True

# ----------------------------

while (running):
    t += dt

    print("Time:", t)

    a = F / m

    dv = a * dt
    v = v + dv

    print("v: ", v)

    dx = v * dt
    x = x + dx

    print("x; ", x)

    # Prevent burning the cqu
    time.sleep(0.1)
    # dedecteerd wanneer de loop moet stoppen
    if x > 100.0:

        running = False  # or use 'Break' to Break out of the loop

# ----------------------------

print("Duration", t, " seconds")

# ----------------------------
