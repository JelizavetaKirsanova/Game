from Config import *
import threading
from EntityClass import EntityClass

class Car(EntityClass):
    def __init__(self, x, y):
        EntityClass.__init__(self)
        self.hight = 50
        self.width = 50
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.point = [0, 0]
        self.path = []
        self.isDoneX = False
        self.isDoneY = False


    def sizeBack(self):
        self.hight = 50
        self.width = 50
        self.image = pg.Surface((50, 50))
        self.timer.cancel()


    def sizePlus(self):
        self.plusScore()
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

