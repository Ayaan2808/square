import pygame

pygame.init()

orange = (252, 157, 3)
height = 600
width = 600
blue = (16, 67, 148)

screen = pygame.display.set_mode((width, height))

runner = True

while runner:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runner = False
    screen.fill(orange)
    square = pygame.draw.rect(screen, blue, pygame.Rect(260, 260 ,80 ,80))
    pygame.display.update()