class Star():
    
    def __init__(self,  color0, diameter, mother = None, angle = None, distance = None):
        self.c = color0
        self.w = diameter
        self.h = diameter
        self.m = mother
        if angle == None or distance == None or mother == None:
            self.m = None
            self.a = None
            self.d = None
        else:
            self.m = mother
            self.a = angle
            self.d = distance
        
    def x(self):
        if self.m != None:
            return self.d * cos(self.a) + self.m.x()
        else:
            return width/2
        
    def y(self):
        if self.m != None:
            return self.d * sin(self.a) + self.m.y()
        else:
            return height/2

    def draw_self(self):
        noStroke()
        fill(self.c)
        ellipse(self.x(), self.y(), self.w, self.h)
        
    
    
        
    