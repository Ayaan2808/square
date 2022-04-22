import pygame

pygame.init()

height = 600
width = 600
white = (255,255,255)
blue = (0,0,255)
x = 250
y = 450

screen = pygame.display.set_mode((height,width))

runner = True

def spaceship(x,y):
    ship = pygame.image.load("img/ship.png")
    ship = pygame.transform.scale(ship, (100, 100))
    screen.blit(ship, (x,y))

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
        explosion_speed = 30
        self.count += 1
        if self.count >= explosion_speed and self.index < len(self.images) - 1:
            self.count = 0
            self.index += 1
            self.image = self.images[self.index]
        if self.index >= len(self.images) - 1 and self.count >= explosion_speed:
            self.kill()
explosion_group = pygame.sprite.Group()

while runner:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runner = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Explosion = explosion(x+40, y-120)
                explosion_group.add(Explosion)
            if event.key == pygame.K_LEFT:
                x = x - 30
            if event.key == pygame.K_RIGHT:
                x = x + 30
    screen.fill(blue)
    spaceship(x,y)
    explosion_group.draw(screen)
    explosion_group.update()
    pygame.display.update()