from inputs import get_gamepad
import time, pygame, sys, os
from Gamepad import PSFOUR

#FACTORY METHOD
def INIT_GAMEPAD(mode="PSFOUR"):
    if mode == "PSFOUR":
        return PSFOUR()

if __name__ == '__main__':

    #init pygame and corresponding controller class
    pygame.init()
    gamepad = INIT_GAMEPAD() 

    #store needed properties
    overlay_img = pygame.image.load(gamepad.get_bg_image())
    display_width = overlay_img.get_width()
    display_height = overlay_img.get_height()
    pygame.display.set_caption('Controller Overlay')

    game_display = pygame.display.set_mode((display_width, display_height))
    button_surface = pygame.Surface((display_width, display_height), pygame.SRCALPHA)
    clock = pygame.time.Clock()
    game_display.fill((255,255,255,255))

    while 1:
        for py_event in pygame.event.get():
            if py_event.type == pygame.QUIT:
                closed = True

        events=get_gamepad()
        for event in events:
            #update state of controller
            gamepad.update(event)
            
            button_surface.fill((0,0,0,0))
            game_display.blit(overlay_img, (0, 0))
            
            gamepad.process_state(pygame,button_surface)
                
            #update display and control frames
            game_display.blit(button_surface, (0,0))
            pygame.display.update()
            clock.tick(60)

    pygame.quit()