#main

import pygame
from wanderlustInvocation import chanceCalculator

backgroundColor = (255, 255, 255)
screenWidth = 500
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Wish Simulator')
screen.fill(backgroundColor)
pygame.font.init()

clock = pygame.time.Clock()

clock.tick(30)

def drawFont(message, centerX, centerY, size, R, G, B):
    text = str(message)
    font1 = pygame.font.SysFont('Times', size)
    text1 = font1.render(text, True, (R, G, B))
    textRect1 = text1.get_rect()
    textRect1.center = (centerX, centerY)
    screen.blit(text1, textRect1)

def wishCircle(center, radius, R, G, B):
    pygame.draw.circle(screen, (R, G, B), center, radius)


def main():
    check = 0
    running = True
    text = "Press Space to Wish"
    wishCount = 0
    wishRed = 0
    wishBlue = 0
    wishGreen = 0
    wishType = ""

    xPos = 100
    yPos = 100

    radius = 30
    cooldown = False
    buffer = 0
    while running:
        screen.fill(backgroundColor)
        if buffer % 5 == 0:
            if cooldown == True:
                if wishType == "5 Star":
                    if wishRed < 255 and wishGreen < 255:
                        wishRed += 1
                        wishGreen += 1
                    else:
                        wishRed = 0
                        wishBlue = 0
                        wishGreen = 0
                        cooldown = False
                elif wishType == "4 Star":
                    if wishRed < 255 and wishBlue < 255:
                        wishRed += 1
                        wishBlue += 1
                    else:
                        wishRed = 0
                        wishBlue = 0
                        wishGreen = 0
                        cooldown = False
                else:
                    if wishBlue < 255:
                        wishBlue += 1
                    else:
                        wishBlue = 0
                        cooldown = False
        buffer += 1
        if xPos < screenWidth and yPos < screenHeight and cooldown is True:
            wishCircle((xPos, yPos), radius, wishRed, wishGreen, wishBlue)
            xPos += 0.2
            yPos += 0.2
        else:
            cooldown = False
            if wishType == "5 Star":
                wishCircle((xPos, yPos), radius, 230,230, 0)
            elif wishType == "4 Star":
                wishCircle((xPos, yPos), radius, 255, 0, 255)
            else:
                wishCircle((xPos, yPos), radius, 0, 0, 230)
            radius += 1
            message = text
            drawFont(message, screenWidth / 2, 400, 30, 0, 0, 0)

        drawFont("Wishes: "+str(wishCount), 50, 20, 20, 0, 0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and cooldown == False:
                    xPos = 70
                    yPos = 70
                    wish, type = chanceCalculator()
                    text = wish
                    wishType = type
                    wishCount += 1
                    cooldown = True
                    radius = 30
                    buffer = 0

        pygame.display.flip()

main()
