import pygame
import random
import time

import numpy as np

img_up = pygame.image.load("up.png")
img_down = pygame.image.load("down.png")
img_left = pygame.image.load("left.png")
img_right = pygame.image.load("right.png")

direction_dict = {1: img_up,
                  2: img_right,
                  3: img_down,
                  4: img_left}


def create_game(surf):
    game_dict = {}
    surf.fill((0, 0, 0))

    for i in range(4):
        for j in range(4):
            choice = random.choice(list(direction_dict.keys()))
            surf.blit(direction_dict[choice], (i * 135 + (i * 5), j * 135 + (j * 5) + 200))
            game_dict[(i, j)] = {'pos_x': i * 135 + (i * 5),
                                 'pos_y': j * 135 + (j * 5) + 200,
                                 'direction': choice}

            pygame.display.flip()

    return game_dict


def flip_arrow(pos):
    pos_i = pos[0] // 135
    pos_j = (pos[1] - 200) // 135

    for i in range(pos_i - 1, pos_i + 2):
        for j in range(pos_j - 1, pos_j + 2):
            if (i, j) in game_dict.keys():
                game_dict[(i, j)]['direction'] = game_dict[(i, j)]['direction'] % 4 + 1
                surf.blit(direction_dict[game_dict[(i, j)]['direction']],
                          (game_dict[(i, j)]['pos_x'], game_dict[(i, j)]['pos_y']))

    pygame.display.flip()


def check_end_game():
    for key, item in game_dict.items():
        if item['direction'] != 1:
            return True

    return False


pygame.init()
surf = pygame.display.set_mode((555, 755))
run = True
game_dict = create_game(surf)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 54)
font_color = pygame.Color('springgreen')
passed_time = 0
timer_started = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(3) == (1, 0, 0):
                timer_started = True
                if timer_started:
                    start_time = pygame.time.get_ticks()

                pos = pygame.mouse.get_pos()
                color = surf.get_at(pos)[:3]
                if color != (0, 0, 0):
                    flip_arrow(pos)
                    run = check_end_game()
    if timer_started:
        passed_time = pygame.time.get_ticks() - start_time

    pygame.draw.rect(surf, (0, 0, 0), pygame.Rect(0, 0, 555, 200))
    text = font.render(str(passed_time / 1000), True, font_color)
    surf.blit(text, (50, 50))
    pygame.display.flip()
    clock.tick(30)

print("Score final : ", str(passed_time / 1000))

pygame.quit()
