import pygame
import random
pygame.init()
pygame.display.set_caption("Platformer + Baseball")
screen = pygame.display.set_mode((700,500))
clock = pygame.time.Clock()

doExit = False

#Link = pygame.image.load('link.png') #load your spritesheet
#Link.set_colorkey((255, 0, 255))

#Constants
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
#A = 0
#D = 1
#W = 2

xpos = 100
ypos = 200
xVel = 10
yVel = 10
keys = [False, False, False, False]
touchGround = False

#Animation
#frameWidth = 64
#frameHeight = 96
#RowNum = 0 
#frameNum = 0
#ticker = 0

CactusHeights= [80,40,20,80,30]

CactusXpos=[]

for x in range(1, 5):

    CactusXpos.append(random.randrange(200, 3000))
    
#CactusImg = pygame.image.load('cactus.png')

while not doExit:###############################################################################################################
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
            
    ypos += yVel

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True              
            if event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            if event.key == pygame.K_UP:
                keys[UP]=True
                

    elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
            elif event.key == pygame.K_UP:
                keys[UP]=False

    #Physics section---------------------------------------------------------------------------------
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT
           
    elif keys[RIGHT]==True:
        vx =+3
    #turn off velocity
    else:
        vx = 0
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP


    CactusXpos = [x - 5 for x in CactusXpos]

    for x in range(len(CactusXpos)):
        if CactusXpos[x]<0:
            CactusXpos[x]=random.randrange(640, 5000)
            print("reset to", CactusXpos[x])
            
    for x, y in zip(CactusXpos, CactusHeights):
        a = pygame.Rect((x, 480-y), (30, 80))
        b = pygame.Rect((xpos, ypos), (30, 30))
        if a.colliderect(b) == True:
            print("Ouch!")

#Collision---------------------------------------------------------------------------------------------------
    if xpos>100 and xpos<200 and ypos+40 >750 and ypos+40 <770:
        ypos = 750-40
        isOnGround = True
        vy = 0
    elif xpos>200 and xpos<300 and ypos+40 >650 and ypos+40 <670:
        ypos = 650-40
        isOnGround = True
        vy = 0
    elif xpos>300 and xpos<400 and ypos+40 >550 and ypos+40 <570:
        ypos = 550-40
        isOnGround = True
        vy = 0
    elif xpos>400 and xpos<500 and ypos+40 >450 and ypos+40 <470:
        ypos = 450-40
        isOnGround = True
        vy = 0
    elif xpos>500 and xpos<600 and ypos+40 >350 and ypos+40 <370:
        ypos = 350-40
        isOnGround = True
        vy = 0
    elif xpos>600 and xpos<700 and ypos+40 >250 and ypos+40 <270:
        ypos = 250-40
        isOnGround = True
        vy = 0
    elif xpos>700 and xpos<800 and ypos+40 >150 and ypos+40 <170:
        ypos = 150-40
        isOnGround = True
        vy = 0
    else:
        isOnGround = False
#Gravity---------------------------------------------------------------------------------------------------------------
    if (ypos+30) > 480:
        touchGround = True
    else:
        touchGround = False
        
    if touchGround == False:
        yVel += 0.5 #gravity
    else:
        yVel = 0

    xpos+=xVel 
    ypos+=yVel
            
    #input section
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and touchGround == True:
        ypos-= 300 #jump

    #Animation----------------------------------------------------------------------------------------
    #if vx < 0: #left animation
        # Ticker is a spedometer. We don't want Link animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
        #RowNum = 0
        #ticker+=1
        #if ticker%10==0: #only change frames every 10 ticks
            #frameNum+=1
           #If we are over the number of frames in our sprite, reset to 0.
           #In this particular case, there are 10 frames (0 through 9)
        #if frameNum>7: 
            #frameNum = 0
  
    #if vx > 0: #left animation
        # Ticker is a spedometer. We don't want Link animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
        #RowNum = 1
        #ticker+=1
        #if ticker%10==0: #only change frames every 10 ticks
            #frameNum+=1
           #If we are over the number of frames in our sprite, reset to 0.
           #In this particular case, there are 10 frames (0 through 9)
        #if frameNum>7: 
            #frameNum = 0
           
    #if vy < 0: #left animation
        # Ticker is a spedometer. We don't want Link animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
            #RowNum = 2
            #ticker+=1
            #if ticker%10==0: #only change frames every 10 ticks
                #frameNum+=1
           #If we are over the number of frames in our sprite, reset to 0.
           #In this particular case, there are 10 frames (0 through 9)
            #if frameNum>7: 
                #frameNum = 0
        
 #render section
    screen.fill((0,0,0))
         
#dino
    pygame.draw.rect(screen, (61, 145, 64), (xpos, ypos, 40, 40), 20)
    
    for x, y in zip(CactusXpos, CactusHeights):
        pygame.draw.rect(screen, (0, 255, 0), (x-15, 480-y, 20, 100))
        #screen.blit(CactusImg, (x-15,480-y))

    pygame.display.flip()
 #end game loop
pygame.quit()
