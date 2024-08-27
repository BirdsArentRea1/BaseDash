import pygame
import math
from BaseDashPlayer import player

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame = pygame.display.set_caption("Base Dash")
clock = pygame.time.Clock()

WHITE = (255, 255,255)
BLUE = (0, 0, 255)

while True: #GAME LOOP ##########################################################################
    clock.tick(60)

#Event handling ---------------------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

#Physics -----------------------------------------------------------------------------------------

#Player movement
if keys[pygame.K_LEFT]:
    px -= vx
    #?
if not jumping and keys[pygame.K_UP]:
    vy = jmp
    jumping = True

vy += g
py += vy

if py >= 600 - ph:
    py = 600 - ph
    jumping = False
    vy = 0

#Render-------------------------------------------------------------------------------------------
screen.fill(WHITE)

pygame.draw.rect(screen, BLUE, (px, py, pw, ph))

pygame.display.flip()

#GAME LOOP END ##################################################################################
