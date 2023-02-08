import pygame

pygame.init()

gameScreen = pygame.display.set_mode((400, 300))

import os

x = 300
y = 100
os.environ['Sp_Video_Window_Pos'] = "%d,%d" % (x, y)

size = [500, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test drawing")
gameScreen.fill((0, 0, 255))
pygame.display.flip()
myImage = pygame.image.load('images/Sky_32.jpg')
myRect = (0, 0, 600, 400)
screen.blit(myImage, myRect)

# Цикл игры
runGame = True # флаг выхода из цикла игры
while runGame:
    # Отслеживание события: "закрыть окно"
    for event in pygame.event.get():
        if event.type == pygame.QUIT: runGame = False

# Выход из игры:
pygame.quit()





