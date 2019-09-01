from random import randint, choice

from math import sqrt


class Ball:
    
    def __init__(self, x, y, size=50):
        self.x = x
        self.y = y
        self.xvel = randint(-5, 5)
        self.yvel = randint(-5, 5)
        self.colors = (color(255,0,0), color(0,255,0))
        self.color = choice(self.colors)
        self.size = size
    
    def move(self):
        self.x += self.xvel
        self.y += self.yvel
        
        if self.x > width or self.x < 0:
            self.xvel = -self.xvel
        
        if self.y > height or self.y < 0:
            self.yvel = -self.yvel
        
        fill(self.color)
        ellipse(self.x, self.y, self.size, self.size)
        fill(0)
        
    def update(self):
        self.move()
        
