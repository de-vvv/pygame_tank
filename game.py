import pygame
import time

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1280, 720])

laser_cooldown = 0.15  # 0.15 seconds between shots
clock = pygame.time.Clock()

tank1 = {'x': 100, 'y': 100, 'width': 50, 'height': 50, 'speed': 5, 'laser': [], 'color': (0, 255, 0), 'last_shot': 0}
tank2 = {'x': 1100, 'y': 600, 'width': 50, 'height': 50, 'speed': 5, 'laser': [], 'color': (0, 0, 255), 'last_shot': 0}

def draw_tank(tank):
    pygame.draw.rect(screen, tank['color'], (tank['x'], tank['y'], tank['width'], tank['height']))

def move_tank(tank, dx, dy):
    tank['x'] = max(0, min(tank['x'] + dx, 1280 - tank['width']))
    tank['y'] = max(0, min(tank['y'] + dy, 720 - tank['height']))

# Function to shoot a laser
def shoot_laser(tank, direction):
    current_time = time.time()
    if current_time - tank['last_shot'] >= laser_cooldown:
        laser = {'x': tank['x'] + tank['width'] // 2, 'y': tank['y'] + tank['height'] // 2, 'speed': direction * 10}
        tank['laser'].append(laser)
        tank['last_shot'] = current_time  # Update the last shot time

def draw_lasers(tank):
    for laser in tank['laser']:
        pygame.draw.circle(screen, (255, 0, 0), (laser['x'], laser['y']), 5)

# Function to update laser positions
def update_lasers(tank):
    for laser in tank['laser']:
        laser['x'] += laser['speed']
    # Remove lasers that go off-screen
    tank['laser'] = [laser for laser in tank['laser'] if 0 <= laser['x'] <= 1280]

# Handle tank movement for both players
def handle_tank_movement(keys, tank, left, right, up, down):
    if keys[left]:
        move_tank(tank, -tank['speed'], 0)  
    if keys[right]:
        move_tank(tank, tank['speed'], 0)  
    if keys[up]:
        move_tank(tank, 0, -tank['speed']) 
    if keys[down]:
        move_tank(tank, 0, tank['speed'])  

# Run until the user asks to quit
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Handle Tank 1 
    handle_tank_movement(keys, tank1, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
    
    # Handle Tank 2 (
    handle_tank_movement(keys, tank2, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)

    if keys[pygame.K_SPACE]:  # Tank 1 shoots to the right
        shoot_laser(tank1, 1)
    if keys[pygame.K_RETURN]:  # Tank 2 shoots to the left
        shoot_laser(tank2, -1)

    
    update_lasers(tank1)
    update_lasers(tank2)
    draw_lasers(tank1)
    draw_lasers(tank2)

    
    draw_tank(tank1)
    draw_tank(tank2)

    # Update the display
    pygame.display.update()

    # Set frame rate
    clock.tick(90)

# Done! Time to quit.
pygame.quit()