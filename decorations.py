import pygame
import random
import Alldecorations

class Grass:

    def __init__(self, window, x, y, hw):
        self.window = window
        self.x = x
        self.y = y
        self.hw = hw
        self.color = (0, random.randint(85, 200), 0)

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.hw, self.hw))


class Tree:
    def __init__(self, window, x, y, hw, blacking):
        self.window = window
        self.x = x
        self.y = y
        self.hw = hw
        self.blacking = blacking
        self.color = (random.randint(30, 120) - self.blacking, random.randint(90, 120) - self.blacking, 0)

        self.x_M = self.x - self.hw/2
        self.x_P = self.x + self.hw/2
        self.y_M = self.y + self.hw

        
    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.hw, self.hw))
