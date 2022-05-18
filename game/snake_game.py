import random
import pygame

pygame.init()

height = 600
width = 600
green = (0,255,0)
red = (255,0,0)
runner = True
over = True
lost = False
pos_x = 270
pos_y = 270
xs = 50
ys = 235
score = 0
lenght = 80
track = 520

def snake():
    global xs
    global ys
    global lenght
    global score
    global runner
    global track
    snake = pygame.draw.rect(screen, red, pygame.Rect(pos_x,pos_y,lenght,40))
    meal = pygame.draw.rect(screen,(0,0,0), pygame.Rect(xs,ys,30,30))
    if pygame.Rect.colliderect(snake, meal):
        score = score+1
        lenght = lenght+10
        track = track-10
        xs = random.randrange(30,540)
        ys = random.randrange(30,540)
    font = pygame.font.Font('freesansbold.ttf', 50)
    points = font.render(f"score : {score}", True, (0,0,0))
    screen.blit(points, (200,0))

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("snake game")

while runner:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runner = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
               pos_y = pos_y+20
            elif event.key == pygame.K_UP:
                pos_y = pos_y-20
            elif event.key == pygame.K_LEFT:
                pos_x = pos_x-20
            elif event.key == pygame.K_RIGHT:
                pos_x = pos_x+20
    if 0<pos_x<height and 0<pos_y<width:
        pass
    else:
       lost = True
    screen.fill(green)
    if score >= 20:
        while over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    over = False
                    runner = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        runner = True
                        over = False
                        score = 0
                        lenght = 80
                        pos_x = 270
                        pos_y = 270
                    elif event.key == pygame.K_q:
                        runner = False
                        over = False
            screen.fill((0,0,255))
            font = pygame.font.Font('freesansbold.ttf', 50)
            fonts = pygame.font.Font('freesansbold.ttf', 30)
            caption = font.render("The snake's belly is full", True, (0,0,0))
            again = fonts.render("Play Again? press p", True, (0,0,0))
            no = fonts.render("Don't wanna play again? press q", True, (0,0,0))
            screen.blit(caption, (10,100))
            screen.blit(again, (20,300))
            screen.blit(no, (20, 500))
            pygame.display.update()
    if lost == True:
        while lost:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    lost = False
                    runner = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        runner = True
                        lost = False
                        score = 0
                        pos_x = 270
                        pos_y = 270
                        lenght = 80
                    elif event.key == pygame.K_q:
                        runner = False
                        lost = False
            screen.fill((0,0,255))
            font = pygame.font.Font('freesansbold.ttf', 50)
            fonts = pygame.font.Font('freesansbold.ttf', 30)
            l_caption = font.render("You lost Try again", True, (0,0,0))
            again = fonts.render("Play Again? press p", True, (0,0,0))
            no = fonts.render("Don't wanna play again? press q", True, (0,0,0))
            screen.blit(l_caption, (10,100))
            screen.blit(again, (20,300))
            screen.blit(no, (20, 500))
            pygame.display.update()
    snake()
    pygame.display.update()