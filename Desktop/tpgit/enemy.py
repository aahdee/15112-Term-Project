import pygame
import random

from gameObject import GameObject

class Enemy(GameObject):
    def __init__(self, x, y):
        super().__init__(x,y, "Textures/enemy.png")
        self.vx = 0
        self.vy = 0
        self.a = 0
        self.xBounds = (0, 700-self.width)
        self.yBounds = (0, 300-self.height)
    
    def paraRandomizer(self):
        vmin, vmax = (-5,5)
        amin, amax = (-0.5,-0.01)
        #a = vmax+1 #always bigger than vy and vx, for the randomizer
        vx = random.uniform(vmin, vmax)
        if vx > 0:
            vy = random.uniform(0, vmax)
        else: 
            vy = random.uniform(vmin, 0)
        a = random.uniform(amin, amax)
        return (vx,vy,a)
    
    def setPara(self):
        self.vx, self.vy, self.a = paraRandomizer()
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        if self.vx < 0:
            self.vx -= self.a
            self.vy -= self.a
        else:
            self.vx += self.a 
            self.vy += self.a
        
        if self.x < self.xBounds[0]:
            self.x = self.xBounds[0]
            self.vx = -self.vx
        elif self.x > self.xBounds[1]:
            self.x = self.xBounds[1]
            self.vx = self.xBounds[1]
        if self.y < self.yBounds[0]:
            self.y = self.yBounds[0]
            self.vy -= self.vy
        elif self.y > self.yBounds[1]:
            self.y = self.yBounds[1]
            self.vy -= self.vy
            
        
        # if self.y < self.yBounds[0] or self.y > self.yBounds[1]:
        #     self.vy = -self.vy