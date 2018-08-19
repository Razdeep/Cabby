import pygame
pygame.init()
gameDisplay=pygame.display.set_mode((800,600))
pygame.display.set_caption('Cabby')
gameOver=False

while not gameOver:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameOver=True
    gameDisplay.fill((128,0,255))
    pygame.display.flip() #updates the screen
    
pygame.quit()
quit()
