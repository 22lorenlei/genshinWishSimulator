#main

import pygame
from wanderlustInvocation import chanceCalculator

backgroundColor = (255, 255, 255)
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Wish Simulator')
screen.fill(backgroundColor)
pygame.font.init()

def drawFont(message):
    text = str(message)
    font1 = pygame.font.SysFont('Arial', 50)
    text1 = font1.render(text, True, (0, 0, 0))
    textRect1 = text1.get_rect()
    textRect1.center = (250, 250)
    screen.blit(text1, textRect1)

def main():
    running = True
    while running:
        screen.fill(backgroundColor)
        message = "something"
        drawFont(message)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    value = chanceCalculator()
                    print(value)

        pygame.display.flip()

main()
