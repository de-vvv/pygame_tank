# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing windo
screen = pygame.display.set_mode([1280,720])
x=100
y=100
a=500
b=500
gun = False
gun2 = False
laser = 0
laser2 = 0
width = 100
speed=5
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\admin\Downloads\Hull_02-removebg-preview.png")  # Load image
        self.rect = self.image.get_rect()  # Get the image's rect
        self.rect.topleft = (x,y)#  initial position

#     def update(self):
#         # Update the sprite's position or other properties
#         pass

player = Player(r"C:\Users\admin\Downloads\Hull_02-removebg-preview.png", 100, 100) 
# Create a sprite group and add the player sprite to it
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
tank = pygame.image.load(r"C:\Users\admin\Downloads\Hull_02-removebg-preview.png")

# Run until the user asks to quit
running = True
while running:
    screen.fill((0,0, 0))

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

    #laser for 1st player
    
    if keys[pygame.K_RETURN]:
        gun2 = True
        laser2=laser2+10


    if (gun2 == True):
        pygame.draw.rect(screen,(250,0,0),(a+laser2,b+50-2.5 ,width+laser2,10))

    if(laser2>20):        
        laser2=laser2+10

    if (laser2 > 1280):
        laser2 = 0
        gun2 = False
    
    #laser for 2nd player

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
    pygame.draw.rect(screen,(250,0,0),(x,y,10,10))
    pygame.draw.rect(screen,(250,0,0),(a,b,100,100))
    screen.blit(tank,(x,y))
    # Update sprites
    # all_sprites.update()

    # # Draw all sprites to the screen
    # all_sprites.draw(screen)
    
    pygame.display.update()

    clock.tick(90)
# Done! Time to quit.
pygame.quit()