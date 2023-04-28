import pygame
pygame.init()
w, h = 1000, 980

player_R = 8
player_X, player_Y = w/2, h/2


def calizia(x, y):
    rect = pygame.Rect(x, y, player_R + player_R/2, player_R + player_R/2)
    return rect


def t(window, x, y, r):
    rect = pygame.Rect(x, y, player_R, player_R)
    return pygame.draw.circle(window, (239, 197, 53), (x, y), r)

def collide(re, ene):
    if re.collidepoint(ene.center):
        return True
    else:
        return False
