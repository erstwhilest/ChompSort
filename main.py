import pygame
import time
import random
import numpy as np

#list all functions that we will be using
# 1. visual/input controls, gets
# 2. functions that will act as our sorting bodies
# 3. sugar code

def start_screen():
    screen = pygame.display.set_mode((1200, 720))
    img = pygame.image.load('CHOMPSORT_ICON_2.jpeg')
    background_colour = (255, 154, 0)
    pygame.display.set_icon(img)
    screen.fill(background_colour)
    t = u"\u2122"
    pygame.display.flip()
    pygame.display.set_caption("ChompSort" + t)
    running = True
    start_screen = True

    Title_font = pygame.font.Font('COOPBL.TTF', 50)
    Title = Title_font.render('Hello', True, (25, 255, 255))

    while running:
        # for loop through the event queue
        # start screen while loop
        while start_screen:
            for event in pygame.event.get():
                # Check for QUIT event
                if event.type == pygame.QUIT:
                    running = False
                    start_screen = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        start_screen = False
            screen.blit(Title, (50, 50))
            pygame.display.update()
def main():
    pygame.init()
    start_screen()


if __name__ == "__main__":
    main()
