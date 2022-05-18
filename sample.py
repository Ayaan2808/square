import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))

img = pygame.image.load("img/user.png")
imgs = pygame.image.load("img/user.png")
runner = True
red = (255,0,0)

rect = img.get_rect()
rect.center = (200, 300)
rects = img.get_rect()
rects.center = (200, 300)

while runner:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runner = False
    screen.fill(red)
    screen.blit(img, rect)
    screen.blit(imgs, rects)
    if pygame.Rect.colliderect(rect,rects):
        print("true")
    pygame.display.update()