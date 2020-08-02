import pygame
import random

#Initialization of Variables
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Just Dodge 4Head')
playerImage = pygame.image.load("player.png")
playerImage = pygame.transform.scale(playerImage, (60, 80))
baronImage = pygame.image.load("baron.png")
baronImage = pygame.transform.scale(baronImage, (200, 300))

font = pygame.font.Font('Font.ttf', 44)
health = 10000
smiteDmg = 700
smiteable = True
x = 400
y = 400
xVel = 0
yVel = 0
speed = 0.5
xDist = 0
yDist = 0
mX = 0
mY = 0

arrived = False


#
def convert(variable, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueConverted = float(variable - leftMin) / float(leftSpan)
    return rightMin + (valueConverted * rightSpan)

#Draws the health bar above Baron Nashor
def healthbar(curHealth):
    damageScale = convert(curHealth, 1, 10000, 0, 248)
    pygame.draw.rect(screen, (255,255,255), (500,200,250,50), 2)
    healthText = font.render(str(curHealth), True, (255, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (502, 202, damageScale, 48), 0)
    screen.blit(healthText, (575, 150))
    screen.blit(baronImage, (530, 300))

#Clears the Screen
def removeBaron():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 800), 0)

#Gets the velocities needed to move the player to the mouse location
def move(xDist, yDist, spd):

    #Sees which direction the player has to travel further in
    maximum = max(abs(xDist), abs(yDist))

    #Creates separate x and y velocities based on the ratio of the x and y distances travelled to
    #ensure that the diagonal speed will allow the player to move to the mouse location
    if maximum == abs(xDist):
        ratio = (abs(xDist) / abs(yDist)) + 1
        print(ratio)
        if xDist > 0:
            if yDist > 0:
                    xVel = spd / ratio * (ratio-1)
                    yVel = spd / ratio
                    return xVel, yVel
            else:
                    xVel = spd / ratio * (ratio-1)
                    yVel = -spd / ratio
                    return xVel, yVel
        if xDist < 0:
            if yDist > 0:
                    xVel = -spd / ratio * (ratio-1)
                    yVel = spd / ratio
                    return xVel, yVel
            else:
                    xVel = -spd / ratio * (ratio-1)
                    yVel = -spd / ratio
                    return xVel, yVel

    elif maximum == abs(yDist):
        ratio = abs(yDist) / abs(xDist)
        print(ratio)
        if xDist > 0:
            if yDist > 0:
                    xVel = spd / ratio
                    yVel = spd / ratio * (ratio-1)
                    return xVel, yVel
            else:
                    xVel = spd / ratio
                    yVel = -spd / ratio * (ratio-1)
                    return xVel, yVel
        if xDist < 0:
            if yDist > 0:
                    xVel = -spd / ratio
                    yVel = spd / ratio * (ratio-1)
                    return xVel, yVel
            else:
                    xVel = -spd / ratio
                    yVel = -spd / ratio * (ratio-1)
                    return xVel, yVel




timeElapsed = 0
clock = pygame.time.Clock()

#Game loop
active = True
while active:
    mX, mY = pygame.mouse.get_pos()
    screen.fill((0,0,0))
    dt = clock.tick()
    healthbar(health)

    #Makes baron take random amounts of damage constantly
    timeElapsed += dt
    if health > 0:
        if timeElapsed > 300:
            damageValue = random.randint(100, 400)
            health -= damageValue
            timeElapsed = 0

    elif health <= 0:
        smiteable = False
        removeBaron()

    #Resets player velocity if the player arrives at the click location
    if arrived == True:
        xVel, yVel = 0, 0

    #Checks for player inputs
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:

                xDist = mX - x
                yDist = mY - y
                xVel, yVel = move(xDist, yDist, speed)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if smiteable:
                    if health < smiteDmg:
                        health -= smiteDmg
                        print("Success!")
                    else:
                        health -= smiteDmg
                        print("KEKW")

    #Moves player to mouse click location with a buffer of 2 pixels (accounts for marginal error in velocity) if they have not arrived
    buffer = 2
    if (x > mX + buffer or x < mX - buffer) and (y < mY - buffer or y > mY + buffer):
        arrived = False
        x += xVel
        y += yVel
    else:
        arrived = True

    screen.blit(playerImage, (x-30,y-40))

    pygame.display.update()
