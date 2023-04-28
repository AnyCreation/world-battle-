import pygame
pygame.init()
w, h = 1000, 980

def calizia(x, y, hw):
    return pygame.Rect(x, y, hw, hw)

def move(rec, px, py, speed):
    rec.x += speed
    return pygame.Rect(rec.x, rec.y, rec.h, rec.w)
