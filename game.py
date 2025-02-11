# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing windo
screen = pygame.display.set_mode([1280,720])
x=250
y=250
a=200
b=200
gun = False
laser = 0
width = 100
speed=5
clock = pygame.time.Clock()
# Run until the user asks to quit
running = True
while running:
    screen.fill((255, 255, 255))
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=speed
    if keys[pygame.K_RIGHT]:
       x+=speed
    if keys[pygame.K_UP]:
       y-=speed
    if keys[pygame.K_DOWN]:
        y+=speed

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        a-=speed
    if keys[pygame.K_d]:
       a+=speed
    if keys[pygame.K_w]:
       b-=speed
    if keys[pygame.K_s]:
        b+=speed

    if keys[pygame.K_RETURN]:
        width=width+1
        pygame.draw.rect(screen,(250,0,0),(x +laser,y+50-2.5 ,width+laser,10))

    if keys[pygame.K_SPACE]:
        gun = True
        laser=laser+10


    if (gun == True):
        pygame.draw.rect(screen,(250,0,0),(x+laser,y+50-2.5 ,width+laser,10))

    if(laser>20):        
        laser=laser+10

    if (laser > 1280):
        laser = 0
        gun = False
    
    # Fill the background with white
 

    # Draw a solid blue circle in the center
    pygame.draw.rect(screen,(250,0,0),(x,y,100,100))
    pygame.draw.rect(screen,(250,0,0),(a,b,100,100))


   
    
    # Flip the display
    pygame.display.update()
    
    clock.tick(90)
# Done! Time to quit.
pygame.quit()