from Config import *

class Walls(pg.sprite.Sprite):
    def __init__(self, x, y, w=50, h=50):
        pg.sprite.Sprite.__init__(self)
        self.width = w
        self.height = h
        self.image = pg.Surface((w, h))
        self.image.fill((128, 128, 128))
        self.rect = self.image.get_rect(center=(x, y))
