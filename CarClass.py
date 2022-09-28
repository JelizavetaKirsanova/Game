from Config import *
import threading


class Car(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.hight = 50
        self.width = 50
        self.image = pg.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.point = [0, 0]
        self.path = []
        self.speed = 1
        self.timer = ""
        self.isDoneX = False
        self.isDoneY = False
        self.score = 0

    def plusScore(self):
        self.score += 10

    def toPlayer(self):
        x = player.rect.x
        y = player.rect.y

        bool = True
        while bool:
            if (x - self.rect.x) % self.speed != 0:
                x = player.rect.x + 1
            if (y - self.rect.y) % self.speed != 0:
                y = player.rect.y + 1

            if (x - self.rect.x) % self.speed == 0 and (y - self.rect.y) % self.speed == 0:
                bool = False

        self.point = [x, y]

    def sizeBack(self):
        self.hight = 50
        self.width = 50
        self.image = pg.Surface((50, 50))
        self.timer.cancel()

    def speedBack(self):
        self.speed = 1
        self.timer.cancel()

    def sizePlus(self):
        if self.hight < 80 and self.width < 80:
            self.hight += 10
            self.width += 10
            if self.timer != "":
                self.image = pg.Surface((self.hight, self.width))
            self.timer = ""
            self.timer = threading.Timer(10.0, self.sizeBack)
            self.timer.start()
        else:
            self.timer.cancel()
            self.timer = threading.Timer(10.0, self.sizeBack)
            self.timer.start()

    def plusSpeed(self):
        if self.speed <= 3:
            self.speed += 1
            self.timer = threading.Timer(10.0, self.speedBack)
            self.timer.start()
        else:
            self.speed = 1
            self.timer.cancel()

    def update(self, x, y):

        if self.rect.y < H:
            pass
        else:
            self.rect.y = 0

        if self.rect.y > -50:
            pass
        else:
            self.rect.y = H + 50

        if self.rect.x < W:
            pass
        else:
            self.rect.x = 0

        if self.rect.x > -50:
            pass
        else:
            self.rect.x = W + 50

        # print(self.point)
        # print(self.path)
        if len(self.path) == 0:
            self.point = [x, y]

        if self.rect.x < self.point[0] - 5:
            self.rect.x += self.speed
        elif self.rect.x > self.point[0] + 5:
            self.rect.x -= self.speed
        else:
            self.isDoneX = True

        if self.rect.y < self.point[1] - 5:
            self.rect.y += self.speed
        elif self.rect.y > self.point[1] + 5:
            self.rect.y -= self.speed
        else:
            self.isDoneY = True

        if self.isDoneX and self.isDoneY and len(self.path) != 0:
            self.point = self.path[0]
            self.path.pop(0)

