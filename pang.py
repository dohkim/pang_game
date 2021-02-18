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


#character set
character=pygame.image.load("C:/Users/tank2/Documents/Local_code/python/pygame_pang/image/character.png")
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=screen_width/2-character_width/2
character_y_pos=screen_height-character_height


pygame.display.set_caption("Pang Game")

#Loop for event
running = True
while running:
    for event in pygame.event.get():        
        if event.type==pygame.QUIT:
            running=False
    
    screen.blit(backgrond, (0,0)) ## screen.fill((0,0,255))
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update()

pygame.quit()