from Star import Star

angle = 0
sun = None
earth = None
moon = None

def setup():
    background('#000000')
    size(800, 600)
    
    global sun, earth, moon
    sun = Star(width/2, height/2, 100, 100, '#E59400')
    earth = Star(width/3 ,height/3, 50, 50, '#003EB2')
    moon = Star(width/4 ,height/4, 20, 20, '#CED6E5')
    earth.set_mother_star(sun)
    moon.set_mother_star(earth)
    
def draw():
    global sun, earth, moon, angle
    background('#000000')
    sun.draw_self()
    earth.draw_self()
    moon.draw_self()
    moon.update_rotate(0.05)    
    earth.update_rotate(0.01) 
    # moon.update_rotate(0.05)