import pygame, sys
import random
import Alldecorations
import player, enemies

pygame.init()
w, h = 1000, 980
wind = pygame.display.set_mode((w, h))

clock = pygame.time.Clock()

list_grass = Alldecorations.grass(320, wind)
list_tree = Alldecorations.tree(150, wind)
#list_enemy = Alldecorations.enemy(45, wind)
enemy = []

speed = 2


En_speed = 0.95

for me in range(14):
    enemy.append(enemies.calizia(random.randint(0, w), random.randint(0, h), 10))

live = 25

run = True
while run:
    clock.tick(80)
    wind.fill((0, 180, 0))
    
    for All_grass in list_grass:
        All_grass.draw()

    Prect = player.calizia(player.player_X, player.player_Y)  
    pygame.draw.rect(wind, (239, 197, 53), Prect)
    player.t(wind, player.player_X + player.player_R / 1.3, player.player_Y + player.player_R / 1.3, player.player_R)

    for touch in enemy:
        if player.collide(Prect, touch):
            live -= 1
            if live <= 0:
                run = False
            

    #print(enemy)
    for rect in enemy:
        pygame.draw.rect(wind, (255, 0, 0), rect)
        if rect.x > player.player_X:
            rect.x -= En_speed
        elif rect.x < player.player_X:
            rect.x += En_speed * 2

        if rect.y > player.player_Y:
            rect.y -= En_speed
        elif rect.y < player.player_Y:
            rect.y += En_speed  * 2

                
    for All_tree in list_tree:
        All_tree[1].draw()
        All_tree[2].draw()
        All_tree[2].draw()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player.player_X >= 0:
        player.player_X -= speed
    elif keys[pygame.K_d] and player.player_X <= w - player.player_R*2:
        player.player_X += speed

    if keys[pygame.K_w] and player.player_Y >= 0:
        player.player_Y -= speed
    elif keys[pygame.K_s] and player.player_Y <= h - player.player_R*2:
        player.player_Y += speed

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
