import pygame

pygame.init()

height = 300
width = 600
white = (255,255,255)
blue = (0,0,255)

screen = pygame.display.set_mode((height,width))

runner = True

def bullets():
    img = pygame.image.load("img/bullet.png")
    img = pygame.transform.scale(img, (50,50))
    pygame.sprite.draw(screen, bgd=None)

while runner:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runner = False
        if event.type == pygame.K_SPACE:
            bullets() 
    screen.fill(blue)
    square = pygame.draw.rect(screen, white, pygame.Rect(100, 100, 100, 100))
    pygame.display.update()