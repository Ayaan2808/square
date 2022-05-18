from cgitb import text
import pygame
import random

pygame.init()

height = 600
width = 600
red = (255,0,0)
x = 520
y = 520
xs = 30
ys = 30
score = 0
done = 0

screen = pygame.display.set_mode((height, width))
runner = True
over = True

def game():
    global xs
    global runner
    global ys
    global score
    global done
    man = pygame.image.load("img/user.png")
    rect = man.get_rect()
    rect.center = (x,y)
    man  = pygame.transform.scale(man, (60,60))
    screen.blit(man, rect)
    burger = pygame.image.load("img/burger.png")
    rects = burger.get_rect()
    rects.center = (xs,ys)
    burger = pygame.transform.scale(burger,(60,60))
    screen.blit(burger, rects)
    if pygame.Rect.colliderect(rect,rects):
        xs = random.randrange(50,550)
        ys = random.randrange(50,550)
        score = score + 1
    if score >= 20:
        done = 1
    font = pygame.font.Font('freesansbold.ttf', 40)
    text = font.render(f"score : {score}", True, (0,0,255))
    screen.blit(text, (300,0))
while runner:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runner = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y = y - 20
            elif event.key == pygame.K_LEFT:
                x = x - 20
            elif event.key == pygame.K_DOWN:
                y = y + 20
            elif event.key == pygame.K_RIGHT:
                x = x + 20
    if 0<=x<=height and 0<=y<=width:
        pass   
    else:
       runner = False
    screen.fill(red)
    if done == 1:
        while over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    over = False
                    runner = False
            font = pygame.font.Font('freesansbold.ttf', 40)
            text_two = font.render("The man has a full belly", True, (0,0,0))
            screen.fill(red)
            screen.blit(text_two, (100,100))
            pygame.display.update()

    game()
    pygame.display.update()