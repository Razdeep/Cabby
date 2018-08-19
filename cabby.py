import pygame
pygame.init()
green=(0,255,0)
gameDisplay=pygame.display.set_mode((800,600))
pygame.display.set_caption('Cabby')
gameOver=False
carImg=pygame.image.load('./assets/car2.png')

while not gameOver:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameOver=True
    gameDisplay.fill(green)
    gameDisplay.blit(carImg,(400,200))
    pygame.display.flip() #updates the screen

pygame.quit()
quit()
