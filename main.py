import pygame

import random
import numpy as np

#list all functions that we will be using
# 1. visual/input controls, gets
# 2. functions that will act as our sorting bodies
# 3. sugar code


def main():
    background_colour = (255, 154, 0)
    screen = pygame.display.set_mode((720,720))
    img = pygame.image.load('CHOMPSORT_ICON_2.jpeg')
    pygame.display.set_icon(img)
    screen.fill(background_colour)
    t = u"\u2122"
    pygame.display.flip()
    pygame.display.set_caption("ChompSort"+t)
    running = True

    while running:
        # for loop through the event queue
        for event in pygame.event.get():
            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.draw.rect(screen, (0, 0, 255), [120, 600, 500, 50])

        pygame.display.update()


if __name__ == "__main__":
    main()
