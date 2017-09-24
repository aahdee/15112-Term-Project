import pygame
from gameObject import GameObject
from hitbox import Hitbox

class Player(GameObject):
    
    def __init__(self,x,y):
       
        super().__init__(x, y,"Textures/play.png")
        self.speed = 4
        self.initSpeed = self.speed
        self.shiftSpeed = 1.5
        self.health = 5
        self.recover = False

        #the hitbox creation
        self.hitboxImg = self.get_image("Textures/hitbox.png")
        self.hitImgW, self.hitImgH = self.hitboxImg.get_size()
        self.hitImgX = self.x+(self.width/2)-(self.hitImgW/2)
        self.hitImgY = self.y+(self.height/2)-(self.hitImgH/2)+1
        
        self.playerHitboxLW = 6 #the Photoshop dimensions
        self.hitX = self.hitImgX+(self.hitImgW-self.playerHitboxLW)/2+1
        self.hitY = self.hitImgY+(self.hitImgH-self.playerHitboxLW)/2
        self.hitbox = Hitbox(self.hitX,self.hitY,"Textures/playerHit.png")
        self.fnt = pygame.font.Font(None, 30)
        self.healthstr = ""
    
    
    def update(self, keysDown):
        key = pygame.key.get_pressed()
        if key[pygame.K_COMMA]:
            self.speed = self.shiftSpeed
        if key[pygame.K_a] and self.hitImgX > 0+self.hitImgW:
            self.x-=self.speed
            self.hitX -= self.speed
        elif key[pygame.K_d] and self.hitImgX < 700-self.hitImgW:
            self.x += self.speed
            self.hitX += self.speed
        if key[pygame.K_w] and self.hitImgY+self.hitImgH > 0+self.hitImgH:
            self.y -= self.speed
            self.hitY -= self.speed
        elif key[pygame.K_s] and self.hitImgY < 700-2*self.hitImgH+self.hitImgH/2:
            self.y += self.speed
            self.hitY+= self.speed
            
        self.speed = self.initSpeed
        
        self.updateRect()
        self.hitbox.update(self.hitX, self.hitY)
        self.hitbox.updateRect()
        
    
    def draw(self, surface):
        if self.recover:
            self.image.set_alpha(128)
            surface.blit(self.image,(self.x,self.y))
            self.image.set_alpha(0)
            surface.blit(self.image,(self.x,self.y))
        else: 
            self.image.set_alpha(0)
            super().draw(surface)
        x = self.x+(self.width/2)-(self.hitImgW/2)+.5
        y = self.y+(self.height/2)-(self.hitImgH/2)+1
        surface.blit(self.hitboxImg, (x, y))
        health = self.fnt.render("health: "+ str(self.health),1,(255,255,255))
        surface.blit(health, (600,10))
        


    def updateRect(self):
        self.hitboxImg = self.get_image("Textures/hitbox.png")
        self.hitImgW, self.hitImgH = self.hitboxImg.get_size()
        self.hitImgX = self.x+(self.width/2)-(self.hitImgW/2)
        self.hitImgY = self.y+(self.height/2)-(self.hitImgH/2)+1
        self.rect = pygame.Rect(self.hitImgX, self.hitImgY, 
                                self.hitImgW, self.hitImgH)
                                #write own collision HA DUB THIS WORKS
        