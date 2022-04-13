from pygame.locals import *
import pygame

pygame.init()

width = 600
height = 600
clock = pygame.time.Clock()
fps = 50

screen = pygame.display.set_mode((width, height))

gray = (64, 55, 32)

def bg():
    screen.fill(gray)

runner = True

class explosion(pygame.sprite.Sprite):
    def __init__ (self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1,6):
            img = pygame.image.load(f"img/exp{num}.png")
            img = pygame.transform.scale(img, (100,100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.count = 0
    def update(self):
        explosion_speed = 4
        self.count += 1
        if self.count >= explosion_speed and self.index < len(self.images) - 1:
            self.count = 0
            self.index += 1
            self.image = self.images[self.index]
        if self.index >= len(self.images) - 1 and self.count >= explosion_speed:
            self.kill()

explosion_group = pygame.sprite.Group()

while runner:
    bg()
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runner = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            Explosion = explosion(pos[0], pos[1])
            explosion_group.add(Explosion)

    explosion_group.draw(screen)
    explosion_group.update()

    pygame.display.update()