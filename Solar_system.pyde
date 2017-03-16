sun = None
earth = None
moon = None

def setup():
    background(0)
    size(800, 600)
    
    noStroke()
    fill('#E59400')
    sun = ellipse(width/2, height/2, 100, 100)
    fill('#003EB2')
    earth = ellipse(width/3 ,height/3, 50, 50)
    fill('#CED6E5')
    moon = ellipse(width/4 ,height/4, 20, 20)
    
def draw():
    fill('#E59400')
    sun = ellipse(width/2, height/2, 100, 100)
    