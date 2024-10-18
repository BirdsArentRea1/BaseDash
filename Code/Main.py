import pygame
import random
from platforms import Platform
from balls import Ball

pygame.init()
pygame.display.set_caption("Base Dash")
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

WHITE = (255, 255,255)
BLUE = (0, 0, 255)

pw, ph = 10, 20
px, py = 50, 50
vx, vy = 5, 0
g = 0.5
jmp = -10
jmp2 = -15
jumping = False
double_jump = False
jump_pressed = False
hit_pressed = False
hitCounter = 0

platforms = []
balls = []

def check_collision(player_x, player_y, player_w, player_h, playforms):
    for platform in platforms:
        if (player_y + player_h <= platform.y and
            player_y + player_h + vy >= platform.y and
            player_x >= platform.x + platform.width and
                player_x <= platform.x + platform.width):
            return platform
        return None


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
    if keys[pygame.K_RIGHT]:
        px += vx
        
    if keys[pygame.K_UP]: #or keys[pygame.K_SPACE]:
        
        if not jump_pressed:
            if not jumping:
                vy = jmp
                jumping = True
            elif not double_jump:
                vy = jmp2
                double_jump = True
            jump_pressed = True
    else:
        jump_pressed = False

#Bat
    if keys[pygame.K_z]:
        hit_pressed = True
        hitCounter = 0

    hitCounter += 1
    if hitCounter > 20:
        hit_pressed = False

#Platform collision
    platform_collided = check_collision(px, py, pw, ph, platforms)
    if platform_collided:
        py = platform_collided.y - ph
        vy = 0
        jumping = False
        double_jump = False
    else:
#apply gravity
        vy += g
        py += vy

    if py >= 600 - ph:
        py = 600 - ph
        jumping = False
        double_jump = False
        vy = 0

#platforms
    if random.randint(1, 100) <= 4:
        platforms.append(Platform())
        # print("appending platform!")

    for platform in platforms:
        if platform.x + platform.width < 100:
            platforms.remove(platform)

#Balls
    if random.randint(1, 100) <= 4:
        balls.append(Ball())
        # print("appending balls!")

    for Ball in balls:
        if Ball.x < 100:
            balls.remove(Ball)

#Render-------------------------------------------------------------------------------------------
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, (px, py, pw, ph))

    for platform in platforms:
        platform.update()
        platform.draw(screen)

    for Ball in balls:
        Ball.update()
        Ball.draw(screen)

    pygame.display.flip()

#GAME LOOP END ##################################################################################
