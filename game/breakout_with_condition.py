import pygame

pygame.init()

screen = pygame.display.set_mode((800,670))
bx = 320
by = 634
x = 300
colors = [(252,3,3), (252, 127, 3), (252, 198, 3), (144, 252, 3), (37, 143, 27), (5, 250, 225), (2, 130, 250), (100, 29, 130), (250, 2, 217),(47, 125, 135)]
def paddel():
    pad = pygame.draw.rect(screen, (255,255,255), pygame.Rect(x,650,80,20))
speed = [1,1]
lis = []

class move():
    def __init__(self, velocity, *args, **kwargs):
        self.velocity = velocity
        self.angle = 0
        super().__init__(*args, **kwargs)
    def move(self):
        self.x += self.velocity
        self.y += self.angle
def game():
    img = pygame.image.load("img/ball.png")
    img = pygame.transform.scale(img, (50,40))
    rect = img.get_rect()
    rect.center = (bx,by)
    screen.blit(img, rect)
    y = 0
    for j in range(7):
        y = y + 50
        xs = -80
        for i in range(10):
            xs = xs+80
            rectangle = pygame.draw.rect(screen, (colors[i]), pygame.Rect(xs,y,80,40))
            lis.append(rectangle)
    for i in range(70):
        if pygame.Rect.colliderect(rect,rectangle):
            print("true")
        
runner = True
while runner:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runner = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 30
            elif event.key == pygame.K_RIGHT:
                x = x + 30
    screen.fill((36,47,56))
    paddel()
    game()
    
    pygame.display.update()