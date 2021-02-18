import pygame
from pygame.display import set_caption



pygame.init() #initialized

#set screen size
screen_width=640
screen_height=480
pygame.display.list_modes()


screen=pygame.display.set_mode((screen_width, screen_height))

#Background image setting
backgrond=pygame.image.load("C:/Users/tank2/Documents/Local_code/python/pygame_pang/image/background.jpg")


pygame.display.set_caption("Pang Game")

#Loop for event
running = True
while running:
    for event in pygame.event.get():        
        if event.type==pygame.QUIT:
            running=False
    
    screen.blit(backgrond, (0,0)) ## screen.fill((0,0,255))
    pygame.display.update()

pygame.quit()