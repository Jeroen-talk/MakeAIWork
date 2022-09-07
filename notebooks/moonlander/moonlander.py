# Open source, license: Apache 2, (C) GEATEC engineering

'''
Requirements:

- Game should simulate landing on the moon with limited amount of fuel
- Should be realtime, obeying laws of physics
- No attitude or lateral control, just vertical thrust
- Show moonscape, lander and motor exhaust in graphical window
- Show velocity, acceleration, motor on/of and fuel in text window
- Toggle motor on/of with mouse click

Testspecs:

- Make a smooth landing
- Make a crash landing
- Relaunch and gain altitude until fuel runs out

Design:

- Moon and Lander are Things in a World
- Picture of moonscape as background
- Lander is a sprite
- Only use standard Python distro >= 3.8, so only turtle graphics
- Single threaded, state machine with varying delta time

'''

import time as tm
import turtle as tr
import random as rd

class Thing:
    def __init__ (self, world):
        self.world = world
        
    def compute (self):
        pass
        
    def render (self):
        pass

class Moon (Thing):
    image = 'moon.gif'

    def render (self):
        if self.world.lander.damage > 0:
            tr.bgpic ('nopic')
            for i in range (int (self.world.lander.damage)):
                tr.bgcolor (rd.choice (('black', 'white', 'red', 'cyan', 'yellow')))
                tm.sleep (0.01)
            tr.bgpic (self.image)
        
class Lander (Thing):    
    normalImage = 'lander_normal.gif'
    firingImage1 = 'lander_firing_1.gif'
    firingImage2 = 'lander_firing_2.gif'

    def __init__ (self, world):
        super () .__init__ (world)
        
        self.y = 90
        self.v = 0
        self.fuel = 50
        
        self.firing = False
        self.touched = False
        
        tr.addshape (self.normalImage)
        tr.addshape (self.firingImage1)
        tr.addshape (self.firingImage2)
        
        tr.onscreenclick (self._toggle)

    def compute (self):
        self.v += self.world.period * (8 if self.firing else -4)
        self.y += self.world.period * self.v
        
        if self.firing:
            self.fuel -= self.world.period * 10
        
        if self.fuel <= 0:
            self.fuel = 0
            self.firing = False
        
        self.damage = 0.1 * self.v * self.v if self.y <= 0 else 0
        
        if self.y < 0:
            if not self.touched:
                tr.title ('The Eagle has ' + (f'CRASHED with velocity {self.v:6.2f} m/s, sorry...' if self.v < -7 else f'landed with velocity {self.v:6.2f} m/s!'))
                self.touched = True
 
            self.firing = False
            self.y = 0
            self.v = 0

    def render (self):
        tr.shape (rd.choice ((self.firingImage1, self.firingImage2)) if self.firing else self.normalImage)
        self.world.goto (0, self.y)
        tr.update ()
        print (f'Height: {self.y:5.2f}      Velocity: {self.v:5.2f}      Firing: {self.firing}      Fuel: {self.fuel:5.2f}') 
        
    def _toggle (self, *args):
        self.firing = not self.firing and self.fuel > 0
        
class World:
    wScreen, hScreen = 1920, 1080
    hImage = 200
    resolution = 0.1    # Meter (in the scene) per pixel
    wScene, hScene = wScreen * resolution , hScreen * resolution
    xTarget, yTarget = -0.035 * wScene, -0.16 * hScene
    
    def __init__ (self):        
        self.moon = Moon (self)
        self.lander = Lander (self)
        self.things = self.moon, self.lander
        
        self._prepare ()
        input ('Press [Enter] to start, click to toggle engine, keep an eye on fuel...')
        self.run ()
        
    def run (self):
        time = tm.time ()
        while True:
            oldTime = time
            time = tm.time ()
            self.period = time - oldTime

            for thing in self.things:
                thing.compute ()

            for thing in self.things:
                thing.render ()
                
            tm.sleep (0.05)
            
    def goto (self, xScene, yScene):
        tr.goto ((xScene + self.xTarget) / self.resolution, (yScene + self.yTarget) / self.resolution - self.hImage)
            
    def _prepare (self):
        tr.setup (self.wScreen, self.hScreen)
        tr.bgpic (self.moon.image)
        tr.title ('Tranquility Base here...')
        tr.speed (0)
        tr.delay (0)
        tr.up ()
        
World ()
                
