import pygame
from random import randint

pygame.init()

def contact(c1, c2):
    return(c1[0] == c2[0] and c1[1] == c2[1])
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Work')
x = 250
y = 250
x1 = 300
y1 = 456
x2 = 230
y2 = 170
x3 = 200
y3 = 140
x4 = 460
y4 = 320

while True:
    pygame.time.delay(10)
    a = randint(-1, 1)
    b = randint(-1, 1)
    a1 = randint(-2, 2)
    b1 = randint(-2, 2)
    a2 = randint(-2, 2)
    b2 = randint(-2, 2)
    a3 = randint(-1, 1)
    b3 = randint(-1, 1)
    a4 = randint(-3, 3)
    b4 = randint(-3, 3)
    pygame.display.flip()
    win.fill(0)
    x += a
    y += b
    x1 += a1
    y1 += b1
    x2 += a2
    y2 += b2
    x3 += a3
    y3 += b3
    x4 += a4
    y4 += b4
    circlepos0 = x
    circlepos1 = y
    circlepos10 = x1
    circlepos11 = y1
    circlepos20 = x2
    circlepos21 = y2
    circlepos30 = x3
    circlepos31 = y3
    circlepos40 = x4
    circlepos41 = y4
    if circlepos0 <= 0:
        circlepos0 = 5
    if circlepos0 >= 499:
        circlepos0 = 494
    if circlepos1 <= 0:
        circlepos1 = 5
    if circlepos1 >= 499:
        circlepos1 = 494
    if circlepos10 <= 0:
        circlepos10 = 5
    if circlepos10 >= 499:
        circlepos10 = 494
    if circlepos11 <= 0:
        circlepos11 = 5
    if circlepos11 >= 499:
        circlepos11 = 494
    if circlepos20 <= 0:
        circlepos20 = 5
    if circlepos20 >= 499:
        circlepos20 = 494
    if circlepos21 <= 0:
        circlepos21 = 5
    if circlepos21 >= 499:
        circlepos21 = 494
    if circlepos30 <= 0:
        circlepos30 = 5
    if circlepos30 >= 499:
        circlepos30 = 494
    if circlepos31 <= 0:
        circlepos31 = 5
    if circlepos31 >= 499:
        circlepos31 = 494
    if circlepos40 <= 0:
        circlepos40 = 5
    if circlepos40 >= 499:
        circlepos40 = 494
    if circlepos41 <= 0:
        circlepos41 = 5
    if circlepos41 >= 499:
        circlepos41 = 494
    #if contact(circlepos0, circlepos10) or contact(circlepos0, circlepos2) or contact(circlepos, circlepos3) or contact(circlepos, circlepos4):
        #x += 10
    #if contact(circlepos1, circlepos) or contact(circlepos1, circlepos2) or contact(circlepos1, circlepos3) or contact(circlepos1, circlepos4):
        #x1 -= 10
    #if contact(circlepos2, circlepos) or contact(circlepos2, circlepos1) or contact(circlepos2, circlepos3) or contact(circlepos2, circlepos4):
        #y2 += 10
    #if contact(circlepos3, circlepos) or contact(circlepos3, circlepos2) or contact(circlepos3, circlepos1) or contact(circlepos3, circlepos4):
        #y3 -= 10
    #if contact(circlepos4, circlepos) or contact(circlepos4, circlepos2) or contact(circlepos4, circlepos3) or contact(circlepos4, circlepos2):
        #y4 += 7
        #x -= 5
    pygame.draw.circle(win, (0, 0, 255), (circlepos0, circlepos1),3, 0)
    pygame.draw.circle(win, (255, 0, 0), (circlepos10, circlepos11), 3, 0)
    pygame.draw.circle(win, (0, 255, 0), (circlepos20, circlepos21), 3, 0)
    pygame.draw.circle(win, (170, 100, 0), (circlepos30, circlepos31), 3, 0)
    pygame.draw.circle(win, (0, 0, 255), (circlepos40, circlepos41), 3, 0)