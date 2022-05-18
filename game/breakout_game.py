import pygame

pygame.init()

screen = pygame.display.set_mode((800,670))

x = 300
colors = [(252,3,3), (252, 127, 3), (252, 198, 3), (144, 252, 3), (37, 143, 27), (2, 250, 167), (2, 130, 250), (176, 2, 250), (250, 2, 217),(47, 125, 135)]

def paddle():
    pad = pygame.draw.rect(screen, (0,0,0), pygame.Rect(x,650,80,20))
def ball():
    img = pygame.image.load("img/ball.png")
    img = pygame.transform.scale(img, (50,40))
    rect = img.get_rect()
    rect.center = (320,630)
    screen.blit(img, rect)
def tile():
    y = 0
    for j in  range(5):
        y = y + 50
        xs = -80
        for i in range(10):
            xs = xs+80
            rectangle = pygame.draw.rect(screen, (colors[i]), pygame.Rect(xs,y,80,40))
            lis = []
            lis.append(rectangle)
runner = True

while runner:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runner = False
    screen.fill((36,47,56))
    paddle()
    ball()
    tile()
    pygame.display.update()