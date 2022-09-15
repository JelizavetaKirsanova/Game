from Functions import *
from random import randint
from ButtonClass import *
from WallsClass import *
from FoodClass import *
import sys
import threading
import math
from Config import *


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


def paused(s, lvl):
    textPar1 = pg.font.SysFont("Roboto", 110)
    surface = textPar1.render(s, True, (0, 0, 0))
    rect = surface.get_rect()
    rect.center = (W / 2, H / 2)
    sc.blit(surface, rect)

    textPar = pg.font.SysFont("Roboto", 50)
    surface = textPar.render("play again", True, (255, 0, 0))
    rect = surface.get_rect()
    x, y = W / 2, H / 2 + 100
    rect.center = (x, y)
    sc.blit(surface, rect)

    surface = textPar.render("menu", True, (255, 0, 0))
    rect = surface.get_rect()
    x, y = W / 2, H / 2 + 200
    rect.center = (x, y)
    sc.blit(surface, rect)

    pg.display.flip()

    pause = True
    while pause:
        if player.clockTimer != "":
            k = player.clockTimer
            if player.timer != "":
                player.timer.cancel()

            for car in cars:
                if car.timer != "":
                    car.timer.cancel()

        for i in pg.event.get():
            if i.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pos()[0] <= x + 100 and pg.mouse.get_pos()[0] >= x - 100 and pg.mouse.get_pos()[
                    1] <= y + 20 and pg.mouse.get_pos()[1] >= y - 20:
                    menu()

                if pg.mouse.get_pos()[0] <= x + 100 and pg.mouse.get_pos()[0] >= x - 100 and pg.mouse.get_pos()[
                    1] <= y - 80 and pg.mouse.get_pos()[1] >= y - 130:
                    run(lvl)

            if i.type == pg.KEYDOWN:
                if i.key == pg.K_ESCAPE:
                    player.clockTimer = k
                    player.timer = threading.Timer(0.1, player.speedBack)
                    player.timer.start()

                    pause = False
            if i.type == pg.QUIT:
                sys.exit()


def run(lvl):
    global player, car1, car2, car3, cars, walls
    f = pg.font.SysFont(None, 30)
    cars = pg.sprite.Group()

    if lvl == 1:
        for i in range(1):
            car = Car(randint(1, W), randint(1, H - 200))
            cars.add(car)

    elif lvl == 3:
        for i in range(5):
            car = Car(randint(1, W), randint(1, H - 200))
            cars.add(car)

    else:
        for i in range(3):
            car = Car(randint(1, W), randint(1, H - 200))
            cars.add(car)

    player = Player()

    food2 = Food(randint(1, W), randint(1, H))
    food2.image.fill((255, 255, 0))
    foods2 = pg.sprite.Group()
    foods2.add(food2)

    food3 = Food(randint(1, W), randint(1, H))
    food3.image.fill((255, 150, 254))
    foods3 = pg.sprite.Group()
    foods3.add(food3)

    food = Food(randint(1, W), randint(1, H))
    foods = pg.sprite.Group()
    foods.add(food)

    PlayerS = pg.sprite.Group()
    PlayerS.add(player)
    walls = pg.sprite.Group()

    for i in range(5):
        wall = Walls(randint(0, W), randint(0, H), 50, 50)
        b = True
        while b:
            b = False
            # if wall.rect.x == 200 and wall.rect.y == 500:
            if ((wall.rect.x <= 200 + 100 and wall.rect.x >= 200 - 100) or (
                    wall.rect.y <= 500 + 100 and wall.rect.y >= 500 - 100)):
                wall = Walls(randint(0, W), randint(0, H), 50, 50)
                b = True

        walls.add(wall)
    listX = []
    listY = []
    while 1:

        sc.fill(WHITE)

        color = (255, 255, 255)
        if player.shield:
            color = (128, 166, 255)

        pg.draw.circle(sc, color, (player.rect.x + 25, player.rect.y + 25), 100)
        pg.draw.circle(sc, (255, 255, 255), (player.rect.x + 25, player.rect.y + 25), 90)

        foods.draw(sc)
        foods2.draw(sc)
        foods3.draw(sc)
        PlayerS.update()
        cars.draw(sc)
        PlayerS.draw(sc)
        foods.update()
        foods2.update()
        walls.draw(sc)

        if player.score >= 100:
            paused("You win!", lvl)
        for car in cars:
            if car.score >= 1000:
                paused("Enemy win!", lvl)

        # player.direction = {"v": "", "h": ""}

        # if len(listX) < 75:
        # listX.append(player.rect.x)

        # if len(listY) < 75:
        # listY.append(player.rect.y)

        # if (len(listX) == 75 and len(listY) == 75) and (sum(listX) / 75 <= listX[0] + 2) and (sum(listY) / 75 <= listY[0] + 2):
        # if (len(listX) == 50 and len(listY) == 50) and ((sum(listX) / 50  > listX[0] + 15 and sum(listY) / 50 > listY[0] + 15) and (listX[0] >= sum(listX) / 50 and listY[0] >= sum(listY) / 50)) or ((sum(listX) / 50 < listX[0] + 15 and sum(listY)/ 50 < listY[0] + 15) and (listX[0] <= sum(listX) / 50 and listY[0] <= sum(listY) / 50)):
        # paused("BUG")
        # elif (len(listX) == 75 and len(listY) == 75):
        # listX = []
        # listY = []

        for wall in walls:
            for car in cars:
                x = car.point[0]
                y = car.point[1]

                if math.sqrt((car.rect.x - wall.rect.x) ** 2 + (car.rect.y - wall.rect.y) ** 2) < 50:
                    x1 = x - car.rect.x
                    y1 = y - car.rect.y

                    if (x1 < 0 and y1 < 0) or (x1 > 0 and y1 > 0):
                        if math.sqrt((car.rect.x - wall.rect.x + 100) ** 2 + (
                                car.rect.y - wall.rect.y + 100) ** 2) < math.sqrt(
                            (car.rect.x - wall.rect.x - 100) ** 2 + (car.rect.y - wall.rect.y - 100) ** 2):
                            x2 = wall.rect.x - 100
                            y2 = wall.rect.y - 100
                            if x2 != car.point[0] and y2 != car.point[1]:
                                car.path.append(car.point)
                                car.point = [x2, y2]
                        else:
                            x2 = wall.rect.x + 100
                            y2 = wall.rect.y + 100
                            if x2 != car.point[0] and y2 != car.point[1]:
                                car.path.append(car.point)
                                car.point = [x2, y2]
                    else:
                        if math.sqrt((car.rect.x - wall.rect.x - 100) ** 2 + (
                                car.rect.y - wall.rect.y + 100) ** 2) < math.sqrt(
                            (car.rect.x - wall.rect.x + 100) ** 2 + (car.rect.y - wall.rect.y - 100) ** 2):
                            x2 = wall.rect.x + 100
                            y2 = wall.rect.y - 100
                            if x2 != car.point[0] and y2 != car.point[1]:
                                car.path.append(car.point)
                                car.point = [x2, y2]
                        else:
                            x2 = wall.rect.x - 100
                            y2 = wall.rect.y + 100
                            if x2 != car.point[0] and y2 != car.point[1]:
                                car.path.append(car.point)
                                car.point = [x2, y2]

            if math.sqrt((player.rect.x - wall.rect.x) ** 2 + (player.rect.y - wall.rect.y) ** 2) < wall.width + 5:
                directions = player.direction
                # print(directions)

                if "down" == directions["v"]:
                    directions["v"] = "up"
                elif "up" == directions["v"]:
                    directions["v"] = "down"

                if "right" == directions["h"]:
                    directions["h"] = "left"

                elif "left" == directions["h"]:
                    directions["h"] = "right"

                # print(directions)
                player.direction = directions

        for car in cars:
            if (player.shield):
                if math.sqrt(
                        (player.rect.x - car.rect.x) ** 2 + (player.rect.y - car.rect.y) ** 2) < 100 + car.width // 2:
                    x = 0
                    y = 0
                    if player.rect.x < car.rect.x:
                        x = W
                    if player.rect.y < car.rect.y:
                        y = H
                    car.speed = player.speed
                    car.update(x, y)
                    car.speed = 1

                elif (getRange(player, car) > getRange(food, car)) and (getRange(food2, car) > getRange(food, car)):
                    car.update(food.rect.x, food.rect.y)
                    car.image.fill((0, 255, 0))

                elif getRange(player, car) > getRange(food2, car) and getRange(food3, car) > getRange(food2, car):
                    car.update(food2.rect.x, food2.rect.y)
                    car.image.fill((255, 255, 0))

                elif getRange(player, car) > getRange(food3, car):
                    car.update(food3.rect.x, food3.rect.y)
                    car.image.fill((255, 150, 254))

                elif math.sqrt((car.rect.x - W // 2) ** 2 + (car.rect.y - H // 2) ** 2) < 50:
                    print("dssd")
                else:
                    car.image.fill((255, 0, 0))
                    car.update(player.rect.x, player.rect.y)



            else:
                if (getRange(player, car) > getRange(food, car)) and (getRange(food2, car) > getRange(food, car)):
                    car.update(food.rect.x, food.rect.y)
                    car.image.fill((0, 255, 0))

                elif getRange(player, car) > getRange(food2, car) and getRange(food3, car) > getRange(food2, car):
                    car.update(food2.rect.x, food2.rect.y)
                    car.image.fill((255, 255, 0))

                elif getRange(player, car) > getRange(food3, car):
                    car.image.fill((255, 150, 254))

                else:
                    car.image.fill((255, 0, 0))
                    car.update(player.rect.x, player.rect.y)

        hits = pg.sprite.spritecollide(player, cars, False)

        if hits and player.shield == False:
            if player.timer != "":
                player.timer.cancel()

            paused("Game over", lvl)

            car1 = Car(randint(1, W), randint(1, H))
            car2 = Car(randint(1, W), randint(1, H))
            car3 = Car(randint(1, W), randint(1, H))

            player = Player()

            food = Food(randint(1, W), randint(1, H))
            foods = pg.sprite.Group()
            foods.add(food)
            foods.add(food2)

            food2 = Food(randint(1, W), randint(1, H))
            food2.image.fill((255, 255, 0))
            foods2 = pg.sprite.Group()
            foods2.add(food2)
            cars = pg.sprite.Group()
            cars.add(car1, car2, car3)

            PlayerS = pg.sprite.Group()
            PlayerS.add(player)

        if pg.sprite.spritecollide(player, foods2, True):
            food2.UpdateLocation()
            foods2.add(food2)
            player.protectAround()

        if pg.sprite.spritecollide(player, foods, True):
            food.UpdateLocation()
            foods.add(food)
            player.plusSpeed()

        if pg.sprite.spritecollide(player, foods3, True):
            food3.UpdateLocation()
            foods3.add(food3)
            player.randomPoint()

        for car in cars:
            if pg.sprite.spritecollide(car, foods, False):
                food.UpdateLocation()
                foods.add(food)
                car.plusScore()
                car.plusSpeed()

            if pg.sprite.spritecollide(car, foods3, False):
                food3.UpdateLocation()
                foods.add(food3)
                car.plusScore()
                car.image.fill((255, 150, 254))

            if pg.sprite.spritecollide(car, foods2, False):
                food2.UpdateLocation()
                foods2.add(food2)
                car.plusScore()
                car.sizePlus()

        for i in pg.event.get():

            if i.type == pg.KEYDOWN:
                if i.key == pg.K_ESCAPE:
                    paused("On pause", lvl)

                if i.key == pg.K_w:
                    if player.direction['v'] == "up":
                        player.direction['h'] = ""
                    else:
                        player.direction['v'] = "up"

                elif i.key == pg.K_s:
                    if player.direction['v'] == "down":
                        player.direction['h'] = ""
                    else:
                        player.direction['v'] = "down"

                if i.key == pg.K_d:
                    if player.direction['h'] == "right":
                        player.direction['v'] = ""
                    else:
                        player.direction['h'] = "right"

                elif i.key == pg.K_a:
                    if player.direction['h'] == "left":
                        player.direction['v'] = ""
                    else:
                        player.direction['h'] = "left"

            if i.type == pg.QUIT:
                for car in cars:
                    if car.timer != "":
                        car.timer.cancel()
                if player.timer != "":
                    player.timer.cancel()
                sys.exit()
        score = str(player.score)

        text = f.render(score, True, (0, 0, 0))
        sc.blit(text, (300, 10))

        for car in cars:
            text = f.render(str(car.score), True, (0, 0, 0))
            sc.blit(text, (car.rect.x, car.rect.y))

        timer = str(player.clockTimer)
        text2 = f.render(timer[:3], True, (0, 0, 0))
        sc.blit(text2, (10, 10))
        pg.display.flip()
        pg.display.update()
        pg.time.delay(20)


def menu():
    while 1:
        sc.fill(WHITE)
        t = pg.font.SysFont("Roboto", 110)
        surface = t.render("Menu", True, (0, 0, 0))
        rect = surface.get_rect()
        rect.center = (W / 2, (H / 2) - 100)
        sc.blit(surface, rect)

        easy = Button(W / 2, H / 2 + 30, 1, "Easy")
        easy.draw()

        medium = Button(W / 2, H / 2 + 80, 2, "Medium")
        medium.draw()

        hard = Button(W / 2, H / 2 + 130, 3, "Hard")
        hard.draw()

        for i in pg.event.get():
            if i.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pos()[0] <= W / 2 + 100 and pg.mouse.get_pos()[0] >= W / 2 - 100 and pg.mouse.get_pos()[
                    1] <= H / 2 + 30 + 20 and pg.mouse.get_pos()[1] >= H / 2 + 30 - 20:
                    run(1)
                if pg.mouse.get_pos()[0] <= W / 2 + 100 and pg.mouse.get_pos()[0] >= W / 2 - 100 and pg.mouse.get_pos()[
                    1] <= H / 2 + 80 + 20 and pg.mouse.get_pos()[1] >= H / 2 + 80 - 20:
                    run(2)
                if pg.mouse.get_pos()[0] <= W / 2 + 100 and pg.mouse.get_pos()[0] >= W / 2 - 100 and pg.mouse.get_pos()[
                    1] <= H / 2 + 130 + 20 and pg.mouse.get_pos()[1] >= H / 2 + 130 - 20:
                    run(3)

        pg.display.flip()

        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()

        pg.display.update()
        pg.time.delay(20)


menu()
