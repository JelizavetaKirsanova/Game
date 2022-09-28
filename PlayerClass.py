from Config import *
import threading
from random import randint


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=(200, 500))
        self.direction = {"v": "down", "h": ""}
        self.speed = 3
        self.timer = ""
        self.clockTimer = 0.0
        self.secondTimer = ""
        self.score = 0
        self.shield = False

    def plusSpeed(self):
        self.score += 10
        if self.timer != "":
            self.timer.cancel()
        self.speed += 1
        self.timer = threading.Timer(0.1, self.speedBack)
        self.timer.start()
        self.clockTimer = 10.0

    def speedBack(self):
        if self.clockTimer < 0:
            self.speed = 3
            self.timer = ""
            self.clockTimer = 0

        else:
            self.timer = threading.Timer(0.1, self.speedBack)
            self.timer.start()
            self.clockTimer -= 0.1

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
        self.score += 10
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

    def randomPoint(self):
        x = randint(1, W)
        y = randint(1, H)

        runp = True

        list = pg.sprite.Group()
        list.add(cars.sprites())
        list.add(walls.sprites())
        while runp:
            runp = False
            for car in list:
                if ((x > car.rect.x + 50 and y > car.rect.y + 50) and (car.rect.x >= x and car.rect.y >= y)) or (
                        (x < car.rect.x + 50 and y < car.rect.y + 50) and (car.rect.x <= x and car.rect.y <= y)):
                    # print("Car: x {0} y {1}\nFood x {2} y {3}".format(car.rect.x, car.rect.y, x ,y))
                    x = randint(1, W)
                    y = randint(1, H)
                    runp = True

        self.rect.x = x
        self.rect.y = y

