import pygame
import random

GREEN = (0, 100, 0)
BLUE = (0, 50, 150)

class Platform:
    def __init__(self):
        self.width = random.randint(140,160)
        self.height = 20
        self.x = 800
        self.y = random.randint(400,550)
        self.speed = random.uniform(3.5,5.5)
        self.type = random.randint(0,2)
        

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        if self.type == 1:
            pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
