import pygame

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
                print("single jump!")
                vy = jmp
                jumping = True
            elif not double_jump:
                print("double jump!")
                vy = jmp2
                double_jump = True
            jump_pressed = True
    else:
        jump_pressed = False

    vy += g
    py += vy

    if py >= 600 - ph:
        py = 600 - ph
        jumping = False
        double_jump = False
        vy = 0


#Render-------------------------------------------------------------------------------------------
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, (px, py, pw, ph))

    pygame.display.flip()

#GAME LOOP END ##################################################################################
