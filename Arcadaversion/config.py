from pygame import *
import os

BASE_DIR = os.path.curdir
IMAGES_DIR = os.path.join(BASE_DIR, 'Images')

mixer.init()
mixer.music.load(os.path.join(IMAGES_DIR, "back_sound2.mp3"))
mixer.music.play(-1)
eneme_crash = mixer.Sound(os.path.join(IMAGES_DIR, "crash.mp3"))


clock = time.Clock()
FPS = 60

win_rez_x = 500
win_rez_y = win_rez_x * 1.5
units_size = win_rez_x // 7
bullets_size = win_rez_x // 80

points = 0

lose = False
win = False

NER = FPS * 1.5
NER_count = 0
NBR = FPS * 0.8
NBR_count = 0

game = True

window = display.set_mode((win_rez_x, win_rez_y))
display.set_caption("Аркада")

end_count = 0


