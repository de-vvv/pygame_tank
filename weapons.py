from settings import *
import time
import math


class weapons:
    def __init__(self):
        self.laser = []
        self.last_shot = 0
        self.laser_cooldown = 0.15

    def shootLaser(self):
        current_time = time.time()
        if current_time - self.last_shot >= self.laser_cooldown:
            laser = {
                "x": self.tankRect.x + self.tankRect.width // 2,
                "y": self.tankRect.y + self.tankRect.height // 2,
                "wx": self.dx,
                "wy": self.dy,
                "speed": 10,
            }
            self.laser.append(laser)
            self.last_shot = current_time

    def drawLasers(self):
        for lasers in self.laser:
            pygame.draw.circle(self.screen, (255, 0, 0), (lasers["x"], lasers["y"]), 5)
            print(self.dx)
            self.laser = [
                lasers for lasers in self.laser if 0 <= lasers["x"] <= CDSIZE[0]
            ]
            lasers["x"] += 8 * lasers["wx"]
            lasers["y"] += 8 * lasers["wy"]
