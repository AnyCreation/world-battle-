import random
import pygame
import decorations

w, h = 1000, 980
#wind = pygame.display.set_mode((w, h))

def grass(i, window):
    grass = []
    for i in range(1, i):
        s = decorations.Grass(window, random.randint(0, w), random.randint(0, h), random.randint(2, 25))
        grass.append(s)

    return grass

def tree(i, window):
    tree = []
    for i in range(1, i):
        s = decorations.Tree(window, random.randint(0, w), random.randint(0, h), random.randint(8, 50), 3)
        t = decorations.Tree(window, s.x + s.hw/4, s.y + s.hw/4, (s.hw / 2) + 2, s.blacking * 3)
        t2 = decorations.Tree(window, (s.x + s.hw/4)/4, (s.y + s.hw)/4, ((s.hw / 2) + 2) + 2, (s.blacking * 3) * 3)
        tree.append([s, t, t2])

    return tree

if __name__ == "__main__":
    print(tree(6, wind))
