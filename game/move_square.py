import pygame

pygame.init()

width = 600
height = 600
orange = (252, 157, 3)
blue = (16, 67, 128)
x = 150
y = 200

screen = pygame.display.set_mode((width, height))

runner = True

while runner:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runner = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-=20
                y = y
            elif event.key == pygame.K_RIGHT:
                x+=20
                y = y
            elif event.key == pygame.K_UP:
                y-=20
                x = x
            elif event.key == pygame.K_DOWN:
                y+=20
                x = x
    square = pygame.draw.rect(screen, blue, pygame.Rect(x,y,10,10))
    pygame.display.flip()