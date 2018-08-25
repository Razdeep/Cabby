import pygame
import obstacle
import random
pygame.init()
clock=pygame.time.Clock()

green=(0,255,0)
DISPLAY_HEIGHT,DISPLAY_WIDTH=800,600
gameDisplay=pygame.display.set_mode((800,600))
pygame.display.set_caption('Cabby')
gameOver=False
carImg=pygame.image.load('./assets/car2.png')
x,y=400,200
x_change=0
obstacle_x,obstacle_y=random.randint(0,DISPLAY_WIDTH),0
obstacle_y_change=0
while not gameOver:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameOver=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change=-5
            elif event.key==pygame.K_RIGHT:
                x_change=5
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or pygame.key==pygame.K_RIGHT:
                x_change=0
    
    gameDisplay.fill(green)
    x=x+x_change
    gameDisplay.blit(carImg,(x,y))

    if obstacle_y_change>DISPLAY_HEIGHT:
        obstacle_x=random.randint(0,DISPLAY_WIDTH)
        obstacle_y_change=0
        
    obstacle.block(gameDisplay,color=(100,100,100),x=obstacle_x,y=obstacle_y+obstacle_y_change)
    obstacle_y_change+=5
    
    # pygame.draw.rect(gameDisplay,(0,0,0),[10,10,100,100])
    pygame.display.flip() #updates the screen
    clock.tick(60)
pygame.quit()
quit()
