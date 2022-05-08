from objects import *
from random import randint

while game:
    clock.tick(FPS)
    keys_pressed = key.get_pressed()

    NER_count += 1
    NBR_count += 1

    window.blit(background, (0, 0))

    player.reset()

    score_count = f1.render(str(points), True, (0, 255, 0))

    if NER_count == NER:
        NER_count = 0
        enemy_generate()

    if NBR_count == NBR:
        NBR_count = 0
        bullers_generate()

    t = win_rez_y - int(win_rez_x // 6)
    w = win_rez_y + 10

    for i in enemies:
        if i.shouted == True:
            i.shouted_time += 1
            if i.shouted_time == 10:
                enemies.remove(i)
                continue

        for j in bullers:
            if sprite.collide_rect(i, j):
                bullers.remove(j)
                points += 1
                i.shouted = True
                eneme_crash.play()
                i.killed()
        if i.rect.y > t and i.rect.y < w:
            enemies.remove(i)
            lose = True
        elif sprite.collide_rect(i, player):
            enemies.remove(i)
            lose = True

    if points >= 10:
        win = True

    if lose == False and win == False:
        window.blit(score, (5, int(win_rez_x // 12)))
        window.blit(score_count, (120, int(win_rez_x // 12)))

    for i in enemies:
        i.reset()
        i.move('down')

    for i in bullers:
        i.reset()
        i.move('up')

    if lose:
        window.blit(text_lose, (int(win_rez_x // 7.27), int(win_rez_x * 3 / 4)))
        # if end_count == 60:
        # time.wait(1000)
        game = False
    if win:
        window.blit(text_win, (int(win_rez_x / 7.27), int(win_rez_x * 3 / 4)))
        game = False

    if keys_pressed[K_LEFT] and player.rect.x > 5:
        player.rect.x -= player.speed
    if keys_pressed[K_RIGHT] and player.rect.x < win_rez_x - 5 - units_size:
        player.rect.x += player.speed

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()