import pygame
pygame.init()
w, h = 1000, 980

player_R = 12
player_R = 8
player_X, player_Y = w/2, h/2

def calizia(window, x, y):
    rect = pygame.Rect(x, y, player_R + player_R/2, player_R + player_R/2)
    return pygame.draw.rect(window, (239, 197, 53), rect)


def t(window, x, y, r):
    rect = pygame.Rect(x, y, player_R, player_R)
    return pygame.draw.circle(window, (239, 197, 53), (x, y), r)
