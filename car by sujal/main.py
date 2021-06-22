import pygame
import random
import time
import math

from pygame.constants import K_RIGHT

pygame.init()
screen=pygame.display.set_mode((800,600))
# timing=time./

#car image

carImg=pygame.image.load('player.png').convert_alpha()
carMImg=pygame.transform.scale(carImg,(50,100))


pygame.display.set_caption('car race game by sujal')
icon=pygame.image.load('enemy.png')
pygame.display.set_icon(icon)

roadImg=pygame.image.load('road.png').convert_alpha()
roadMImg=pygame.transform.scale(roadImg,(1700,600))
# a=pygame.Surface.get_size(roadImg)

enemyImg=pygame.image.load('enemy.png').convert_alpha()
enemyMImg=pygame.transform.scale(enemyImg,(100,150))

#player
playerX=380
playerY=400
#enemy
enemyX=random.randint(275,450)
enemyY=-600
enemy_speed=1.3



#game over
over=pygame.image.load('over.png')
finish=pygame.transform.scale(over,(400,400))
# #background
roadX=-450
roadY1=0
roadY2=-600
road_speed=0.2

def crash(enemyX,enemyY,playerX,playerY):
    distance=math.sqrt(math.pow(playerX-enemyX,2)+math.pow(playerY-enemyY,2))
    if distance<60:
        return True
    else:
        return False  

def mycar(playerX,playerY):
    screen.blit(carMImg,(playerX,playerY))

def enemy(enemyX,enemyY):
    screen.blit(enemyMImg,(enemyX,enemyY))

def way(roadX,roadY1):
    screen.blit(roadMImg,(roadX,roadY1))
    screen.blit(roadMImg,(roadX,roadY1-600))

def game_over():
    screen.blit(finish,(300,200))


moving=True
while moving:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            moving=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX-=120
            if event.key==pygame.K_RIGHT:
                playerX+=120


        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or K_RIGHT:
                playerX+=0
                

        if playerX>=510 or playerX<250:
            moving=False 
            

    screen.fill((0,0,0))
    way(roadX,roadY1) 
    roadY1+=road_speed
    roadY2+=road_speed
    if roadY1>=600:
        roadY1=0
    # way(roadX,roadY2)
    # roadY2=-road_speed

    collision=crash(enemyX, enemyY, playerX, playerY)
    if collision:
        moving=False
        # if game_over():
        #     time.sleep(2)


    enemy(enemyX,enemyY) 
    enemyY+=enemy_speed
    if enemyY>=600:
        enemyX=random.randint(220,450)
        enemyY=-600
    if not moving:
        game_over()
        

    enemy(enemyX,enemyY)
    mycar(playerX,playerY)
    # timing.tick(30)
    pygame.display.update()
