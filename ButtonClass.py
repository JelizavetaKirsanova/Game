from Config import *

class Button(pg.sprite.Sprite):
    def __init__(self, x, y, lvl, text):
        pg.sprite.Sprite.__init__(self)
        self.lvl = lvl
        self.x = x
        self.y = y
        self.text = text
        self.image = pg.Surface((100, 20))
        self.image.fill((100, 0, 0))
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self):
        t = pg.font.SysFont("Roboto", 50)
        surface = t.render(self.text, True, (0, 0, 0))
        rect = surface.get_rect()
        rect.center = (self.x, self.y)
        sc.blit(surface, rect)

    def click(self, run):
        for i in pg.event.get():
            if i.type == pg.MOUSEBUTTONDOWN:
                if self.x + 100 >= pg.mouse.get_pos() >= self.x - 100 and self.y + 20 >= pg.mouse.get_pos() >= self.y - 20:
                    run(self.lvl)
