from settings import *
from weapons import *
import math


class tank(weapons):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.speed = 3
        self.angle = 0
        self.dx = 0
        self.dy = 0

        self.tank = pygame.image.load(
            "assets/tankBody_dark_outline.png"
        ).convert_alpha()
        self.tankRect = self.tank.get_rect(center=(x, y))

    def drawTank(self):
        self.rotatedTank = pygame.transform.rotozoom(self.tank, self.angle + 90, 1.0)
        self.rotatedRect = self.rotatedTank.get_rect(center=self.tankRect.center)
        self.screen.blit(self.rotatedTank, self.rotatedRect)
        self.drawLasers()

    def updateHead(self):
        radians = math.radians(self.angle)
        self.dx = -1 * math.cos(radians)
        self.dy = math.sin(radians)

    def moveTank(self, head):
        self.updateHead()
        self.tankRect.x = max(
            0,
            min(
                self.tankRect.x + self.speed * self.dx * head,
                CDSIZE[0] - self.tankRect.width,
            ),
        )
        self.tankRect.y = max(
            0,
            min(
                self.tankRect.y + self.speed * self.dy * head,
                CDSIZE[1] - self.tankRect.height,
            ),
        )

    def handleMovements(self, keys, left, right, up, down, fire):
        if keys[left]:
            self.angle += 5
            self.updateHead()
        if keys[right]:
            self.angle -= 5
            self.updateHead()
        if keys[up]:
            self.moveTank(1)
        if keys[down]:
            self.moveTank(-1)
        if keys[fire]:
            self.updateHead()
            self.shootLaser()
        self.drawTank()


clock = pygame.time.Clock()

tank1 = tank(SCREEN, 100, 100)
tank2 = tank(SCREEN, 1100, 500)


# NOTE:(zxie): while loop starts
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

    # Update the display
    pygame.display.update()

    clock.tick(90)


pygame.quit()
