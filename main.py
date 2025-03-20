from settings import *
import time


class tank:
    def __init__(self, screen, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.color = color
        self.speed = 5

        # weapons specific variables
        self.laser = []
        self.last_shot = 0
        self.laser_cooldown = 0.15

    def drawTank(self):
        tank = pygame.image.load("assets/tankBody_dark_outline.png").convert_alpha()
        self.screen.blit(tank, [self.x, self.y])
        # pygame.draw.rect(
        #     self.screen, self.color, (self.x, self.y, self.width, self.height)
        # )

    # def blitTank(self):

    def moveTank(self, dx, dy):
        self.x = max(0, min(self.x + dx, CDSIZE[0] - self.width))
        self.y = max(0, min(self.y + dy, CDSIZE[1] - self.height))

    def handleMovements(self, keys, left, right, up, down, fire):
        self.drawTank()
        if keys[left]:
            self.moveTank(-self.speed, 0)
        if keys[right]:
            self.moveTank(self.speed, 0)
        if keys[up]:
            self.moveTank(0, -self.speed)
        if keys[down]:
            self.moveTank(0, self.speed)
        if keys[fire]:
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
        for lasers in self.laser:
            pygame.draw.circle(self.screen, (255, 0, 0), (lasers["x"], lasers["y"]), 5)
            # Remove lasers that go off-screen
            self.laser = [
                lasers for lasers in self.laser if 0 <= lasers["x"] <= CDSIZE[0]
            ]
            lasers["x"] += lasers["speed"]


clock = pygame.time.Clock()


tank1 = tank(SCREEN, 100, 100, 50, 55, RED)
tank2 = tank(SCREEN, 1100, 500, 50, 55, BLUE)


# Run until the user asks to quit
while RUNNING:
    KEYS = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.VIDEORESIZE:
            if not FLSCR:
                SCREEN = pygame.display.set_mode([event.w, event.h], pygame.RESIZABLE)
                CDSIZE = [event.w, event.h]

    if KEYS[pygame.K_LSUPER] and KEYS[pygame.K_f]:
        FLSCR = not FLSCR
        if FLSCR:
            SCREEN = pygame.display.set_mode(DSIZE, pygame.FULLSCREEN)
            CDSIZE = DSIZE
        else:
            SCREEN = pygame.display.set_mode(
                [SCREEN.get_width(), SCREEN.get_height()], pygame.RESIZABLE
            )

    SCREEN.fill((0, 0, 0))
    tank1.handleMovements(
        KEYS, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE
    )
    tank2.handleMovements(
        KEYS, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_RETURN
    )

    tank1.drawLasers()
    tank2.drawLasers()
    # tank1.blitTank()

    # Update the display
    pygame.display.update()

    clock.tick(90)


pygame.quit()
