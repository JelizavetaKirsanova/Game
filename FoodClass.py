import random
from Config import *

class Food(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))

    def UpdateLocation(self):
        self.rect.x = random.randint(0, W)
        self.rect.y = random.randint(0, H)
