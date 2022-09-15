import pygame as pg

W = 600
H = 600
WHITE = (255, 255, 255)

pg.font.init()
pg.init()
pg.mixer.init()

sc = pg.display.set_mode((W, H))
pg.display.set_caption("Test Game")


