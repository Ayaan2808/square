import pygame
pygame.init()
colors = (255,0,0)
color = (0,0,255)
width = 600
height = 600
screen = pygame.display.set_mode((width,height))
runner = True
x = 200
y = 200

class rectangle:
    def make_rect(self):
        pygame.draw.circle(screen, color, (x,y), 15)
rects = rectangle()

while runner:
    for event in pygame.event.get():
        print("x",x)
        print("y",y)
        if event.type == pygame.QUIT:
            runner = False
    if x < width or x > 0:
        y = y + 0.2
        x = x + 0.2

    if y > height - 7.5 or y < 0:
        print("previous", x,y)
        y = y - 0.2
        x = x - 0.2
        
    screen.fill(colors)
    rects.make_rect()
    pygame.display.update()