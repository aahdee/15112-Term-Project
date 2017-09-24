import pygame
import random
from frame import PygameGame
from gameObject import GameObject
from Bullet import Bullet
from player import Player
from hitbox import Hitbox
from enemy import Enemy
from bulletFunc import circle, spiral, multiSpiOnePoint, multiCircle, paramRandomizer

class Game(PygameGame):
        
    def init(self):
        #splash screen things
        self.mainmenu = True
        self.start = False
        self.help = False
        self.pause = False
        self.gameOver = False
        self.newHSBool = False
        self.fnt = pygame.font.Font(None, 35)
        self.endfnt = pygame.font.Font(None, 180)
        self.pausetime = 0
        self.file = open("save.txt","r")
        self.highScore = self.file.readline()
        
        self.HSX = 625
        self.HSY = 13
        self.NHSX = 190
        self.NHSY = 420 #ay
        
        self.menuColor = (24,113,163)
        
        #background source: http://pics-about-space.com/green-nebula?p=1
        self.gameBG = self.get_image("Textures/background.png")
        self.menuScreen = self.get_image("Textures/menu.png")
        self.helpScreen = self.get_image("Textures/help.png")
        self.pauseScreen = self.get_image("Textures/pause.png")
        self.gameoverScreen = self.get_image("Textures/gameover.png")
        self.newHS = self.get_image("Textures/hsmessage.png")
        
        self.player = Player(200, 650)
        
        self.functions = [circle, spiral, multiSpiOnePoint,multiCircle]
        
        self.funk1 = None
        self.funk2 = None
        self.funk3 = None
        
        
        #for the resetting the functions
        self.new1 = False
        self.new2 = False
        self.new3 = False
        self.first = True
        
        self.move = False
        self.enemyturn = 2
        
        self.score = 0
        self.recoverTimerSet = False
        
        self.funcCall = 10
        #funk3 has a random mod. changes when its called. to add more **surprises**
        self.funk3RNG = random.randint(1, self.funcCall-2) 
        #number of funcions (funk1, funk2, etc). Might add more functions.
        self.funcNum = 2
        
        self.enemy = Enemy(350,200)
    
    
    
    def redrawAll(self, screen):
        #things that are drawn depending on the splash screen bools
        if self.mainmenu:
            screen.blit(self.menuScreen,(0,0))
            score = self.fnt.render(self.highScore,1,self.menuColor)
            screen.blit(score,(self.HSX,self.HSY))
        
        if self.help:
            screen.blit(self.helpScreen,(0,0))
        
        if self.start:
            screen.blit(self.gameBG, (0,0))
            
            self.player.draw(screen)
            
            #heh
            if self.funk1 != None: self.funk1.draw(screen)
            if self.funk2 != None: self.funk2.draw(screen)
            if self.funk3 != None: self.funk3.draw(screen)
            
            self.enemy.draw(screen)
            elasped = self.fnt.render("Score: "+ str(self.seconds),1,(255,255,255))
            screen.blit(elasped,(10,10))
        
        if self.pause:
            screen.blit(self.pauseScreen,(0,0))
            
        if self.gameOver:
            screen.blit(self.gameoverScreen,(0,0))
            score = self.endfnt.render(str(self.score),1,self.menuColor)
            screen.blit(score, (300,320))
            if self.newHSBool:
                screen.blit(self.newHS, (self.NHSX,self.NHSY))
            
        
    
    def timerFired(self, dt):
        
        keypressed = pygame.key.get_pressed()
        if self.mainmenu:
            self.seconds = 0
            if keypressed[pygame.K_p]:
                self.mainmenu = False
                self.start = True
            elif keypressed[pygame.K_i]:
                self.mainmenu = False
                self.help = True
            elif keypressed[pygame.K_q]:
                self.mainmenu = False
                pygame.quit()
                return True
        
        elif self.help:
            if keypressed[pygame.K_m]:
                self.mainmenu = True
                self.help = False
        
        elif self.start:
            if self.seconds%60 < 10: self.showSec = "0" + str(self.seconds%60)
            else: self.showSec = str(self.seconds%60)
            self.showMin = str(self.seconds//60)
            if keypressed[pygame.K_ESCAPE]:
                self.pausetime = self.seconds 
                self.start = False
                self.pause = True

            else:
                #player movement
                self.player.update(self.isKeyPressed)
                #enemy movement
                if self.seconds%self.enemyturn == 0 and self.move == False:
                    self.enemy.vx, self.enemy.vy, self.enemy.a = self.enemy.paraRandomizer()
        
                    self.move = True
                
                if self.seconds%self.enemyturn == self.enemyturn -1:
                    self.move = False
                
                self.enemy.update()
                def newfunc(self):
                    index = random.randint(0, len(self.functions)-1)
                    para = paramRandomizer(self.enemy.x + self.enemy.width/2, 
                                            self.enemy.y + self.enemy.height/2)
                    
                    return self.functions[index](*para)
            
                #funk1 START call
                if self.seconds%self.funcCall == 0 and self.new1 == False and self.first:
                    self.funk1 = newfunc(self)
                    self.new1 = True
                    self.first = False
                
                #funk2 call
                elif (self.seconds%self.funcCall == self.funcCall//self.funcNum
                and self.new2 == False):
                    self.funk2 = newfunc(self)
                    self.new2 = True
                
                #funk3 call
                elif (self.seconds%self.funcCall == self.funk3RNG and self.new3 == False):
                    self.funk3 = newfunc(self)
                    self.new3 = True
                    
                #funk1 REST call
                elif self.seconds%self.funcCall == 0 and self.new1 == False:
                    self.funk1 = newfunc(self)
                    self.new1 = True
                
                #funk1 reset    
                elif (self.seconds %self.funcCall == self.funcCall-1 
                            and self.seconds != 0 and self.new1):
                    self.new1 = False
                
                #funk2 reset
                elif self.seconds % self.funcCall == self.funcCall//self.funcNum-1 and self.new2:
                    self.new2 = False
                    
                #funk3 reset 
                if (self.seconds%self.funcCall == self.funk3RNG-1 and
                    self.seconds>self.funcCall and self.new3):
                    self.new3 = False
                    self.funk3RNG = random.randint(1, self.funcCall-1)
                    
                    
                #collision
                if self.funk1 != None:
                    for bullet in self.funk1:
                        if (pygame.sprite.collide_circle(bullet.hitbox, self.player.hitbox) and 
                            self.player.recover == False):
                            self.player.health -= 1
                            self.player.recover = True
                    
                    self.funk1.update()
                
                if self.funk2 != None:
                    for bullet in self.funk2:
                        if (pygame.sprite.collide_circle(bullet.hitbox, self.player.hitbox) 
                            and self.player.recover == False):
                            self.player.health -= 1
                            self.player.recover = True
                    
                    self.funk2.update()
                
                if self.funk3 != None:
                    for bullet in self.funk3:
                        if (pygame.sprite.collide_circle(bullet.hitbox, self.player.hitbox)
                            and self.player.recover == False):
                            self.player.health -= 1
                            self.player.recover = True
                    
                    self.funk3.update()
                
                if self.player.health == 0:
                    self.start = False
                    self.gameOver = True
            
                #player recover
                if self.player.recover:
                    
                    if self.recoverTimerSet == False:
                        pygame.time.set_timer(pygame.USEREVENT+2, 1000)
                        self.recoverTimerSet = True
                    
                    for event in pygame.event.get():
                        if event.type == pygame.USEREVENT+2:
                            self.player.recover = False
                            self.recoverTimerSet = False
                
                if self.player.health == 0:
                    self.score = self.seconds
                    
        elif self.pause:
            self.seconds = self.pausetime
            if keypressed[pygame.K_r]:
                self.pause = False
                self.start = True
                
        elif self.gameOver:
            if self.score > int(self.highScore):
                file = open("save.txt","w")
                file.write(str(self.score))
                file.close()
                self.newHSBool = True
                
            if keypressed[pygame.K_r]:
                self.init()
            elif keypressed[pygame.K_q]:
                pygame.quit()
                return True
                
        return False
                
#for dramatic effect play this video before you run: https://www.youtube.com/watch?v=69AyYUJUBTg
game = Game()
game.run()
        