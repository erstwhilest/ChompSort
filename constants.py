import pygame
pygame.font.init()

def tup_sub(tup1, tup2):
    return (tup1[0]-tup2[0], tup1[1]-tup2[1])

def tup_add(tup1, tup2):
    return (tup1[0]+tup2[0], tup1[1]+tup2[1])

SORT_NAMES=["Radix Sort", "Bitonic Sort", "Pancake Sort", "Cocktail Shaker Sort", "Stooge Sort", "Cycle Sort"]

# SCREEN_RES = (1920, 1080)
SCREEN_RES = (1280, 720)
# GAME_RES = (1280, 720)
# GAME_BORDER = (0, GAME_RES[1]/12)
# SCREEN_RES = tup_add(GAME_RES, GAME_BORDER)
# BTN_BORDER = int(GAME_RES[0]/360)+1
# BTN_PAD = int(GAME_RES[0]/72)
BTN_BORDER = int(SCREEN_RES[0]/360)+1
BTN_PAD = int(SCREEN_RES[0]/72)
FONT = "CascadiaMono.ttf"

YPAD = SCREEN_RES[0]/48

# Colors
BLACK = (0, 0, 0)
EXTRA_LIGHT_GRAY = (212, 212, 212)
LIGHT_GRAY = (128, 128, 128)
GRAY = (64, 64, 64)
WHITE = (255, 255, 255)
ORANGE = (255, 128, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Dynamic font sizes
LBL_FSIZE = int(SCREEN_RES[0]/20)
SML_LBL_FSIZE = int(SCREEN_RES[0]/30)

BTN_FSIZE = int(SCREEN_RES[0]/60)
LRG_BTN_FSIZE = int(SCREEN_RES[0]/30)

NUMBERS = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]

THUMB_SIZE = (15, 30)
TRACK_HEIGHT = 5