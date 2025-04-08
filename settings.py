import pygame

pygame.init()

# NOTE:(zxieeee) Defining colors

RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)


# NOTE:(zxieeee) Defining global variables
RUNNING = True
FLSCR = False
DSIZE = [pygame.display.Info().current_w, pygame.display.Info().current_h]
SCREEN = pygame.display.set_mode([1280, 720], pygame.RESIZABLE)
CDSIZE = DSIZE
