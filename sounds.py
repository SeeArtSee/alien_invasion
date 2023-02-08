import pygame as pg
import sys

pg.init()
sc = pg.display.set_mode((400, 300))

pg.mixer.music.load('music/GAME-003.WAV')
pg.mixer.music.play()

sound1 = pg.mixer.Sound('music/GAME-011.WAV')
sound2 = pg.mixer.Sound('music/Game-008.Wav')

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

        elif i.type == pg.KEYUP:
            if i.key == pg.K_DOWN:
                pg.mixer.music.pause()
                # pygame.mixer.music.stop()
            elif i.key == pg.K_UP:
                pg.mixer.music.unpause()
                # pygame.mixer.music.play()
                pg.mixer.music.set_volume(0.5)
            elif i.key == pg.K_LEFT:
                pg.mixer.music.unpause()
                # pygame.mixer.music.play()
                pg.mixer.music.set_volume(1)

        elif i.type == pg.MOUSEBUTTONUP:
            if i.button == pg.BUTTON_LEFT:
                sound1.play()
            elif i.button == pg.BUTTON_RIGHT:
                sound2.play()

    pg.time.delay(20)