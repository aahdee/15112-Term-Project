import pygame
from gameObject import GameObject
from hitbox import Hitbox

class Bullet(GameObject):
    def __init__(self,x,y,speedx, speedy):
        super().__init__(x,y, "Textures/bullet.png")
        self.speedx = speedx
        self.speedy = speedy
        self.radius = self.height/2
        self.bulletHitboxLW = 8 #i created it to be 8 px
        self.hitX = self.x - self.radius+1
        self.hitY = self.y -self.radius+1
        self.hitbox = Hitbox(self.hitX,
                             self.hitY,
                             "Textures/bulletHit.png")
                                
    def update(self):
        self.y += self.speedy
        self.x += self.speedx
        self.hitX += self.speedx
        self.hitY += self.speedy
        
        self.updateRect()
        self.hitbox.update(self.hitX, self.hitY)
        self.hitbox.updateRect()
    
        