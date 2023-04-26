import pygame, sys
import random
import Alldecorations
import player

pygame.init()
w, h = 1000, 980
wind = pygame.display.set_mode((w, h))

clock = pygame.time.Clock()

list_grass = Alldecorations.grass(320, wind)
list_tree = Alldecorations.tree(150, wind)

speed = 2

while True:
    clock.tick(80)
    wind.fill((0, 180, 0))
    
    for All_grass in list_grass:
        All_grass.draw()

    player.t(wind, player.player_X + player.player_R / 1.3, player.player_Y + player.player_R / 1.3, player.player_R)
    player.calizia(wind, player.player_X, player.player_Y)

        
    for All_tree in list_tree:
        All_tree[1].draw()
        All_tree[2].draw()
        All_tree[2].draw()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.player_X -= speed
    elif keys[pygame.K_d]:
        player.player_X += speed

    if keys[pygame.K_w]:
        player.player_Y -= speed
    elif keys[pygame.K_s]:
        player.player_Y += speed

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
