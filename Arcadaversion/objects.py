from classes import *
from random import randint

import os

background = transform.scale(image.load(os.path.join(IMAGES_DIR, 'background.jpg')), (win_rez_x, win_rez_y))

player = Unit(os.path.join(IMAGES_DIR, 'x-wing.png'), win_rez_x / 2 - units_size / 2, win_rez_y * 7 / 8, units_size, 10)

def enemy_generate():
    enemies.append(Unit(os.path.join(IMAGES_DIR, 'CID.png'),
                    randint(5, int((win_rez_x - units_size - 5))), 0, units_size, 2))
enemies = []
def bullers_generate():
    bullers.append(Unit(os.path.join(IMAGES_DIR, 'Bullet.png'),
                    player.rect.x + units_size / 2 - bullets_size / 2, player.rect.y, bullets_size, 2))
bullers = []

init()
f1 = font.SysFont("comicsansms", int(win_rez_x / 13.3))
f2 = font.SysFont("arialblack", int(win_rez_x // 8))

score = f1.render("Score:", True, (255, 0, 0))
score_count = f1.render(str(points), True, (0, 255, 0))

text_lose = f2.render("You're lose", True, (0, 0, 255))
text_win = f2.render("You're win", True, (0, 0, 255))