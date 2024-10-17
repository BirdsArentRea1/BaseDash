import pygame
import random

WHITE = (255, 255, 255)

class Ball:
    def __init__(self):
        self.x = 800
        self.y = random.randint(400,550)
        self.speed = random.uniform(3.5,5.5)
        self.type = random.randint(0,2)
        

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        if self.type == 1:
            pygame.draw.circle(screen, WHITE, (self.x, self.y), 5)
        else:
            pygame.draw.circle(screen, WHITE, (self.x, self.y), 5)
