# This would be shortly available
import pygame
def obstacle(gameDisplay,color=(0,0,0),x=10,y=10,height=100,width=100):
    pygame.draw.rect(gameDisplay,color,[x,y,height,width])
    return