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


#destination coordinate
to_x=0
to_y=0

#Loop for event
running = True
while running:
    for event in pygame.event.get():        
        if event.type==pygame.QUIT:
            running=False

        #Key event
        if event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_LEFT:
                to_x -= 1 
            elif  event.key == pygame.K_RIGHT:
                to_x += 1 
            elif  event.key == pygame.K_UP:
                to_y -= 1 
            elif  event.key == pygame.K_DOWN:
                to_y += 1 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                to_x=0
            elif event.key == pygame.K_UP or pygame.K_DOWN:
                to_y=0

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos=0
    elif character_x_pos > screen_width-character_width:
        character_x_pos=screen_width-character_width
    elif character_y_pos < 0:
        character_y_pos=0
    elif character_y_pos > screen_height-character_height:
        character_y_pos=screen_height-character_height

    screen.blit(backgrond, (0,0)) ## screen.fill((0,0,255))
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update()

pygame.quit()