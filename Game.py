import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Game')
playerImage = pygame.image.load("player.png")
playerImage = pygame.transform.scale(playerImage, (50, 50))


x = 400
y = 400
xVel = 0
yVel = 0
speed = 0.3
xDist = 0
yDist = 0
mX = 0
mY = 0

def player(x,y):
    screen.blit(playerImage, (x,y))

def move(xDist, yDist, spd):

    maximum = max(abs(xDist), abs(yDist))

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





active = True

startTime = pygame.time.get_ticks()
while active:
    screen.fill((0,0,0))
    time = pygame.time.get_ticks()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                mX, mY = pygame.mouse.get_pos()
                xDist = mX - x
                yDist = mY - y
                xVel, yVel = move(xDist, yDist, speed)


    buffer = 2
    if (x > mX + buffer or x < mX - buffer) and (y < mY - buffer or y > mY + buffer):
        x += xVel
        y += yVel

    player(x,y)
    pygame.display.update()
