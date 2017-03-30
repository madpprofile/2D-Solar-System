from Star import Star

sun, earth, moon = None, None, None

def setup():
    size(800, 600)
    
    global sun, earth, moon
    sun = Star('#E59400', 100)
    earth = Star('#003EB2', 50, sun, 0, width/4)
    moon = Star('#CED6E5', 20, earth, 0, width/12)
    
def draw():
    global sun, earth, moon
    background('#000000')
    sun.draw_self()
    earth.draw_self()
    moon.draw_self()
    moon.a += 0.05
    earth.a += 0.01