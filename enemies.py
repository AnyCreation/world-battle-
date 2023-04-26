import pygame
pygame.init()
w, h = 1000, 980

class Enemies:

    def __init__(self, window, x, y, hw, speed, live, D_list):
        self.window = window
        self.x = x
        self.y = y
        self.hw = hw
        self.speed = speed
        self.live = live
        self.D_list = D_list

        self.rect = pygame.Rect(self.x, self.y, self.hw, self.hw)

    def dead(self):
        if self.live <= 0:
            self.D_list.remove(self)


    def draw(self):
        pygame.draw.rect(self.window, (130, 0, 0), self.rect)
