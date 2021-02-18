import pygame
from pygame.display import set_caption



pygame.init() #initialized

#set screen size
screen_width=480
screen_height=640
pygame.display.list_modes()


screen=pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Pang Game")

#Loop for event
running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

pygame.quit()