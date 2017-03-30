class Star():
    
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        self.m = None
    
    def draw_self(self):
        noStroke()
        fill(self.c)
        ellipse(self.x, self.y, self.w, self.h)
        
    def set_mother_star(self, s):
        self.m = s
        
    def origemX(self):
        if self.m == None:
            return 0
        else:
            return self.m.origemX() + self.m.x    

    def origemY(self):
        if self.m == None:
            return 0
        else:
            return self.m.origemY() + self.m.y    
        
                        
    def update_rotate(self, angle):
        ox = self.origemX()
        oy = self.origemY()
        nx = ((self.x - ox) * cos(angle) - (self.y - oy) * sin(angle)) + ox
        ny = ((self.x - ox) * sin(angle) + (self.y - oy) * cos(angle)) + oy
        self.x = nx
        self.y = ny
        