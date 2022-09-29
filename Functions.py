import math

from Config import x_center, sc
from Config import y_center
import pygame as pg


def getRange(a, b):
    return math.sqrt((a.rect.x - b.rect.x) ** 2 + (a.rect.y - b.rect.y) ** 2)


def isClickInPos(clickcoord, *args):
    return x_center + args[0] >= clickcoord[0] >= x_center + args[1] and y_center + args[2] >= clickcoord[
        1] >= y_center + args[3]


def createTextBlock(text, font="Roboto", fontsize=50, color=(0, 0, 0), x_shift=0, y_shift=0):
    textpar = pg.font.SysFont(font, fontsize)
    surface = textpar.render(text, True, color)
    rect = surface.get_rect()
    rect.center = (x_center + x_shift, y_center + y_shift)
    sc.blit(surface, rect)
