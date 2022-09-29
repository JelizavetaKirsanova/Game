import pygame as pg

W = 600
H = 600
x_center, y_center = W / 2, H / 2
WHITE = (255, 255, 255)

pg.font.init()
pg.init()
pg.mixer.init()

sc = pg.display.set_mode((W, H))
pg.display.set_caption("Test Game")


