import pygame
from pygame.locals import *
screen = pygame.display.set_mode((600,600))
color = (0,0,255)
class ball:
    global runner
    def __init__(self,x,y):
        self.radius = 20
        self.x = x - self.radius
        self.y = y
        self.speed_x = 4
        self.speed_y = -4
        self.square = Rect(self.x,self.y,self.radius*2,self.radius*2)
    def draw(self):
        self.balll = pygame.draw.circle(screen, color, (self.square.x + self.radius, self.square.y + self.radius), self.radius)
    def move(self):
        global runner
        if self.square.left < 0 or self.square.right > 600:
            self.speed_x *= -1
        if self.square.top < 0:
            self.speed_y *= -1
        if self.square.bottom > 600:
            runner = False
            print("You lost")
        self.square.x = self.square.x + self.speed_x
        self.square.y = self.square.y + self.speed_y