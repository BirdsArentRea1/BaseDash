import pygame
import random

class Platform:
    def __init__(self):
        self.width = random.randint(140,160)
        self.height = 20
        self.x = 800
        self.y = random.randint(400,550)
        self.speed = random.uniform(3.5,5.5)
        self.color = (random.randint(0, 255), random.randint(0 ,255), random.randint(0, 255))
        self.has_base = random.randint(1,100) <= 30
        
    def update(self):
        self.x -= self.speed

    def draw(self, screen):
            
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

            if self.has_base:
                 pygame.draw.rect(screen, self.color, (self.x + 50, self.y - 40, 20, 40))
