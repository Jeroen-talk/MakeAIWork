import time as tm

running = True
t = 0
dt = 0.1

while (running):
    t += dt
    tm.sleep(0.1)
    # equivalent t_new = t_old + dt
    # eqiuvalent t = t + dt
    print("Time:", t)
