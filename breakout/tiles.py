import pygame
colors = [(100,3,3), (252, 127, 3), (252, 198, 3), (144, 252, 3), (37, 143, 27), (5, 250, 225)]
xs = 0
y = 0
class tiles:
    def __init__(self, screen, colors, xs, y):
        self.screen = screen
        self.colors = colors
        self.xs = xs
        self.y = y
        self.tile = pygame.Rect(xs,y,100,40)
        self.lis = []
        self.draw(xs,y)
    def draw(self,xs,y):
        for j in range(7):
            y = y + 50
            xs = -100
            for i in range(6):
                xs = xs+100
                self.rectangle = pygame.draw.rect(self.screen, (colors[i]), pygame.Rect(xs,y,100,40))
                self.lis.append(self.rectangle)