import pygame
from gameObject import GameObject

class Hitbox(GameObject):
    
    def __init__(self,x,y,image):
        super().__init__(x,y, image)
    
    def update(self, newx, newy):
        self.x = newx
        self.y = newy
