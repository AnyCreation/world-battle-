import pygame
import random
w, h = 1000, 980

def hp(window, live):
    list_font = pygame.font.get_fonts()
    #print(list_font[4])

    zh = 15
    zw = live * 4 
    #200
    pygame.draw.rect(window, (35, 35, 35), (10, 10, 25, 248))
    pygame.draw.rect(window, (120, 40, 40), (15, 15, zh, zw))

    hp = str(live)
    f1 = pygame.font.Font(None, 22)
    AL = f1.render(hp, False, (255, 255, 255))
    window.blit(AL, (15, 100))


def armor(window, ar):
    le = str(ar)
    a = (34 / 2) * len(le)
    pygame.draw.rect(window, (150, 150, 150), (15, h - 45, a, 34))


    far = pygame.font.Font(None, 40)
    AL = far.render(le, False, (255, 255, 255))
    window.blit(AL, (17, h - 41))