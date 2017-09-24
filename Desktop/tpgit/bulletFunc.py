import pygame
import math
import random
from Bullet import Bullet

#randomizes the parameters for the functions. 
def paramRandomizer(x,y):
    minBullets, maxBullets = (30, 350) #any more and things get wonky and uber hard
    minAngle, maxAngle = (0, 360) 
    minDeltaR, maxDeltaR = (0.007,0.03) #after playtesting, this is the best max/min
    minAngDiv, maxAngDiv = (2,8) #best after playtesting
    
    bulletNum = random.randint(minBullets, maxBullets)
    deltaR = random.uniform(minDeltaR, maxDeltaR)
    shift = random.randint(0,1)
    angDivider = random.randint(minAngDiv, maxAngDiv)
    angle = random.randint(minAngle, maxAngle)
    intbool = random.randint(0,1)
    neg = True if intbool else False
    rand = random.randint(0,1)
    if rand == 0: num = 2
    else: num = 4 
    return [bulletNum, x,y, shift, angle, num, angDivider, deltaR,neg]
    
## These functions take in extra params that they dont need. This is to allow
## the randomizer to work for all functions and not have a randomizer for every 
## function that I create.
 

#returns a circle
def circle(bulletNum, x,y, shift, angle, num, angDivider, deltaR,neg):
    angle = 0 if shift%2 == 0 else (360/bulletNum)/2
    deltaAng = 360/bulletNum
    bulletGroup = pygame.sprite.Group()
    for i in range(bulletNum):
        deltaY = 2*math.sin(angle*math.pi/180)
        deltaX = 2*math.cos(angle*math.pi/180)
        bulletGroup.add(Bullet(x,y,deltaX, deltaY))
        angle += deltaAng
    return bulletGroup

#returns a single sprial at one point
def spiral(bulletNum, x,y, shift, angle, num, angDivider, deltaR,neg):
    r = 2
    deltaAng = 360/(bulletNum/angDivider)
    if neg: deltaAng *= -1
    bulletGroup = pygame.sprite.Group()
    for i in range(bulletNum):
        deltaX= r*math.cos(angle*math.pi/180)
        deltaY = r*math.sin(angle*math.pi/180)
        bulletGroup.add(Bullet(x,y,deltaX, deltaY))
        r += deltaR
        angle += deltaAng
    return bulletGroup

#returns a group of sprials focused at one point
def multiSpiOnePoint(bulletNum, x,y, shift, angle, num, angDivider, deltaR,neg):
    bulletGroup = pygame.sprite.Group()
    deltaAng = 360/(num)
    if neg: deltaAng *= -1
    bullets = bulletNum//num
    for i in range(num):
        bulletGroup.add(spiral(bullets, x,y, shift, angle, num, angDivider, deltaR,neg))
        angle += deltaAng
    return bulletGroup

#returns a group of multi circles
def multiCircle(bulletNum, midx,y, shift, angle, num, angDivider, deltaR,neg):
    bulletGroup = pygame.sprite.Group()
    angle = 0
    enemyW = 90
    deltaAng = 360/bulletNum
    bullets = bulletNum//num
    distance = random.randint(100, 200)
    if num % 2 == 1:
        startX = midx - distance*(num//2)
    else:
        startX = midx - (distance*(num//2)) +enemyW-enemyW/4
    for i in range(num):
        bulletGroup.add(circle(bullets, startX,y, shift, 
                            angle, num, angDivider, deltaR,neg))
        startX += distance
    return bulletGroup

