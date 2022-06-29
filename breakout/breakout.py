import pygame
from pygame.locals import *
from Ball import ball
from tiles import tiles
from paddle import paddlee
pygame.init()

colors = (255,0,0)
color = (0,0,255)
width = 600
height = 600
colours = [(252,3,3), (252, 127, 3), (252, 198, 3), (144, 252, 3), (37, 143, 27), (5, 250, 225), (2, 130, 250), (100, 29, 130), (250, 2, 217),(47, 125, 135)]
y = 0
xs = 0
fps = 60
x = 300
matrix = [[0,0,0,0,0,0]]

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Breakout game")
runner = True

clock = pygame.time.Clock()

tile = tiles(screen,colors,xs,y)
rects = ball(100,560)
pads = paddlee()

while runner:
    clock.tick(fps)
    screen.fill(colors)
    rects.draw()
    rects.move()
    tile.draw(xs,y)
    pads.paddel(x)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runner = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 30
            elif event.key == pygame.K_RIGHT:
                x = x + 30
    if pygame.Rect.colliderect(pads.pad,rects.balll):
        rects.speed_y *= -1
    for i in range(41):
        if pygame.Rect.colliderect(rects.balll, tile.lis[i]):
            rects.speed_y *= -1
    pygame.display.update()