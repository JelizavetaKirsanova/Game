from Config import *
import threading
from random import randint
from EntityClass import EntityClass


class Player(EntityClass):
    def __init__(self):
        EntityClass.__init__(self)
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=(200, 500))
        self.direction = {"v": "down", "h": ""}
        self.shield = False

    def update(self):
        if "down" == self.direction["v"]:
            if self.rect.y < H:
                self.rect.y += self.speed
            else:
                self.rect.y = 0
        elif "up" == self.direction["v"]:
            if self.rect.y > -50:
                self.rect.y -= self.speed
            else:
                self.rect.y = H + 50
        if "right" == self.direction["h"]:
            if self.rect.x < W:
                self.rect.x += self.speed
            else:
                self.rect.x = 0
        elif "left" == self.direction["h"]:
            if self.rect.x > -50:
                self.rect.x -= self.speed
            else:
                self.rect.x = W + 50

    def protectAround(self):
        self.plusScore()
        if self.timer != "":
            self.timer.cancel()
        self.timer = threading.Timer(0.1, self.protect)
        self.shield = True
        self.timer.start()
        self.clockTimer = 10.0

    def protect(self):
        if self.clockTimer < 0.1:
            self.shield = False
            self.timer = ""
            self.clockTimer = 0
        else:

            self.timer = threading.Timer(0.1, self.protect)
            self.timer.start()
            self.clockTimer -= 0.1


