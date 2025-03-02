import pygame
import time
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1280, 720])

laser_cooldown = 0.15  # 0.15 seconds between shots
clock = pygame.time.Clock()

tank1_image = pygame.image.load('tank1.png')
tank2_image = pygame.image.load('tank2.png')

tank1_image = pygame.transform.scale(tank1_image, (50, 50))
tank2_image = pygame.transform.scale(tank2_image, (50, 50))

tank1 = {'x': 100, 'y': 100, 'width': 50, 'height': 50, 'speed': 5, 'laser': [], 'color': (0, 255, 0), 'last_shot': 0, 'health': 100}
tank2 = {'x': 1100, 'y': 600, 'width': 50, 'height': 50, 'speed': 5, 'laser': [], 'color': (0, 0, 255), 'last_shot': 0, 'health': 100}

# Drawing the tank
def draw_tank(tank):
    pygame.draw.rect(screen, tank['color'], (tank['x'], tank['y'], tank['width'], tank['height']))

# Moving the tank and keeping it within bounds
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

# Function to draw lasers
def draw_lasers(tank):
    for laser in tank['laser']:
        pygame.draw.circle(screen, (255, 0, 0), (laser['x'], laser['y']), 5)

# Function to update laser positions
def update_lasers(tank):
    for laser in tank['laser']:
        laser['x'] += laser['speed']
    # Remove lasers that go off-screen
    tank['laser'] = [laser for laser in tank['laser'] if 0 <= laser['x'] <= 1280]

# Check for laser collision with tanks
def check_laser_collision(tank1, tank2):
    # Check if any laser from tank1 hits tank2
    for laser in tank1['laser']:
        if tank2['x'] < laser['x'] < tank2['x'] + tank2['width'] and tank2['y'] < laser['y'] < tank2['y'] + tank2['height']:
            # Collision detected, decrease health of tank2
            tank2['health'] -= 10  # Damage dealt by laser (can be changed)
            tank1['laser'].remove(laser)  # Remove the laser after it hits
            break  # Stop checking after the first collision

    # Check if any laser from tank2 hits tank1
    for laser in tank2['laser']:
        if tank1['x'] < laser['x'] < tank1['x'] + tank1['width'] and tank1['y'] < laser['y'] < tank1['y'] + tank1['height']:
            # Collision detected, decrease health of tank1
            tank1['health'] -= 10  # Damage dealt by laser (can be changed)
            tank2['laser'].remove(laser)  # Remove the laser after it hits
            break  # Stop checking after the first collision

# Handle tank movement for both players
def handle_tank_movement(keys, tank, left, right, up, down):
    if keys[left]:
        tank['x'] -= tank['speed']
    if keys[right]:
        tank['x'] += tank['speed']
    if keys[up]:
        tank['y'] -= tank['speed']
    if keys[down]:
        tank['y'] += tank['speed']

    # Ensure tank stays within screen bounds (0 <= x <= 1280, 0 <= y <= 720)
    tank['x'] = max(0, min(tank['x'], 1280 - tank['width']))
    tank['y'] = max(0, min(tank['y'], 720 - tank['height']))

# Run until the user asks to quit
running = True
while running:
    screen.fill((0, 0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Handle Tank 1 (WASD controls)
    handle_tank_movement(keys, tank1, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
    
    # Handle Tank 2 (Arrow keys)
    handle_tank_movement(keys, tank2, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)

    # Shooting mechanics
    if keys[pygame.K_SPACE]:  # Tank 1 shoots to the right
        shoot_laser(tank1, 1)
    if keys[pygame.K_RETURN]:  # Tank 2 shoots to the left
        shoot_laser(tank2, -1)

    # Update and draw lasers
    update_lasers(tank1)
    update_lasers(tank2)
    draw_lasers(tank1)
    draw_lasers(tank2)

    # Check for laser collisions and update health
    check_laser_collision(tank1, tank2)

    # Draw the tanks
    draw_tank(tank1)
    draw_tank(tank2)

    # Display health bars
    font = pygame.font.SysFont(None, 30)
    health_text1 = font.render(f"Health: {tank1['health']}", True, (0, 255, 0))
    screen.blit(health_text1, (tank1['x'], tank1['y'] - 20))
    health_text2 = font.render(f"Health: {tank2['health']}", True, (0, 0, 255))
    screen.blit(health_text2, (tank2['x'], tank2['y'] - 20))

    # Win condition check
    if tank1['health'] <= 0:
        print("Tank 2 wins!")
        running = False  # End the game if tank1 is out of health
    if tank2['health'] <= 0:
        print("Tank 1 wins!")
        running = False  # End the game if tank2 is out of health

    # Update the display
    pygame.display.update()

    # Set frame rate
    clock.tick(90)

# Done! Time to quit.
pygame.quit()
