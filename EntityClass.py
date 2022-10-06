from Config import *
import threading
from random import randint


class EntityClass(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        # self.image.fill((0, 0, 255))
        # self.rect = self.image.get_rect(center=(200, 500))
        # self.direction = {"v": "down", "h": ""}
        self.speed = 3
        self.timer = ""
        self.clockTimer = 0.0
        self.score = 0
        # self.shield = False

    def plusScore(self):
        self.score += 10

    def plusSpeed(self):
        self.plusScore()
        if self.timer != "":
            self.timer.cancel()
        if self.speed <= 5:
            self.speed += 1
        self.timer = threading.Timer(0.1, self.speedBack)
        self.timer.start()
        self.clockTimer = 10.0

    def speedBack(self):
        if self.clockTimer < 0:
            self.speed = 1
            self.timer = ""
            self.clockTimer = 0

        else:
            self.timer = threading.Timer(0.1, self.speedBack)
            self.timer.start()
            self.clockTimer -= 0.1

    def update(self):
        pass

    def randomPoint(self, cars, walls, playerS):
        x = randint(1, W)
        y = randint(1, H)

        runp = True

        list = pg.sprite.Group()
        list.add(cars.sprites())
        list.add(walls.sprites())
        list.add(playerS.sprites())
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
