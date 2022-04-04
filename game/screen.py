import pygame

pygame.init()

width = 600
height = 600
orange = (252, 157, 3)

screen = pygame.display.set_mode((width, height))

runner = True

while runner:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runner = False
    screen.fill(orange)
    pygame.display.update()