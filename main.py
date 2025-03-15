import pygame
import time

pygame.init()

# NOTE:(zxieeee) Defining colors

RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)


# NOTE:(zxieeee) Defining global variables
WIDTH = 1280
HEIGHT = 720
RUNNING = True
FLSCR = False
DISIZE = [pygame.display.Info().current_w, pygame.display.Info().current_h]


KEYS = pygame.key.get_pressed()
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT], pygame.RESIZABLE)


class tank:
    def __init__(self, screen, keys, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.color = color
        self.speed = 5
        self.keys = keys

        # weapons specific variables
        self.laser = []
        self.last_shot = 0
        self.laser_cooldown = 0.15

    def drawTank(self):
        pygame.draw.rect(
            self.screen, self.color, (self.x, self.y, self.width, self.height)
        )

    # def blitTank(self):
    # tank = pygame.image.load("assets/tankBody_dark_outline.png").convert_alpha()
    # blit

    def moveTank(self, dx, dy):
        self.x = max(0, min(self.x + dx, 1280 - self.width))
        self.y = max(0, min(self.y + dy, 720 - self.height))

    def handleMovements(self, left, right, up, down, fire):
        self.drawTank()
        if self.keys[left]:
            self.moveTank(-self.speed, 0)
        if self.keys[right]:
            self.moveTank(self.speed, 0)
        if self.keys[up]:
            self.moveTank(0, -self.speed)
        if self.keys[down]:
            self.moveTank(0, self.speed)
        if self.keys[fire]:
            self.shootLaser(1)

    # NOTE:(zxieeee):  Have plans to make a separete class called weapons
    def shootLaser(self, direction):
        current_time = time.time()
        if current_time - self.last_shot >= self.laser_cooldown:
            laser = {
                "x": self.x + self.width // 2,
                "y": self.y + self.height // 2,
                "speed": direction * 10,
            }
            self.laser.append(laser)
            self.last_shot = current_time  # Update the last shot time

    def drawLasers(self):
        # self.shootLaser(1)
        for lasers in self.laser:
            pygame.draw.circle(self.screen, (255, 0, 0), (lasers["x"], lasers["y"]), 5)
            # Remove lasers that go off-screen
            self.laser = [lasers for lasers in self.laser if 0 <= lasers["x"] <= 1280]
            lasers["x"] += lasers["speed"]


clock = pygame.time.Clock()


tank1 = tank(SCREEN, KEYS, 100, 100, 50, 55, RED)
tank2 = tank(SCREEN, KEYS, 1100, 500, 50, 55, BLUE)


# Run until the user asks to quit
while RUNNING:
    SCREEN.fill((200, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.VIDEORESIZE:
            if not FLSCR:
                SCREEN = pygame.display.set_mode([event.w, event.h], pygame.RESIZABLE)

    if KEYS[pygame.K_LSUPER] and KEYS[pygame.K_f]:
        FLSCR = not FLSCR
        if FLSCR:
            SCREEN = pygame.display.set_mode([DSIZE], pygame.FULLSCREEN)
        else:
            SCREEN = pygame.display.set_mode(
                [SCREEN.get_width(), SCREEN.get_height()], pygame.RESIZABLE
            )

    tank1.handleMovements(
        pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE
    )
    tank2.handleMovements(
        pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_RETURN
    )

    tank1.drawLasers()
    tank2.drawLasers()
    # tank1.blitTank()

    # Update the display
    pygame.display.update()

    clock.tick(90)


pygame.quit()
