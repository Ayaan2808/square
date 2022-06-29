import pygame
screen = pygame.display.set_mode((600,600))
class paddlee:
    def paddel(self,x):
        self.x = x 
        self.pad = pygame.draw.rect(screen, (255,255,255), pygame.Rect(x,580,80,20))