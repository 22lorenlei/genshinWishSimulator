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
    running = True
    text = "Press Space to Wish"
    count = 0
    wishRed = 0
    wishBlue = 130
    wishGreen = 0
    wishType = ""
    while running:
        screen.fill(backgroundColor)
        wishCircle((screenWidth / 2, screenHeight / 2), 30, wishRed, wishGreen, wishBlue)
        message = text
        drawFont(message, screenWidth / 2, 400, 30, 0, 0, 0)
        drawFont("Wishes: "+str(count), 50, 20, 20, 0, 0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    wish, type = chanceCalculator()
                    text = wish
                    wishType = type
                    if type == "5 Star":
                        wishRed = 255
                        wishGreen = 215
                        wishBlue = 0
                    elif type == "4 Star":
                        wishRed = 255
                        wishGreen = 0
                        wishBlue = 215
                    else:
                        wishRed = 0
                        wishGreen = 0
                        wishBlue = 215
                    count += 1

        pygame.display.flip()

main()
