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

def drawFont(message, centerX, centerY, size, R, G, B):
    text = str(message)
    font1 = pygame.font.SysFont('Times', size)
    text1 = font1.render(text, True, (R, G, B))
    textRect1 = text1.get_rect()
    textRect1.center = (centerX, centerY)
    screen.blit(text1, textRect1)

def main():
    running = True
    text = "Press Space to Wish"
    count = 0
    while running:
        screen.fill(backgroundColor)
        message = text
        drawFont(message, screenWidth / 2, 400, 30, 0, 0, 0)
        drawFont("Wishes: "+str(count), 50, 20, 20, 0, 0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    value = chanceCalculator()
                    text = value
                    count += 1

        pygame.display.flip()

main()
