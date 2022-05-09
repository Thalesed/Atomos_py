import pygame
from random import randint
import sys

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Atomo')
a =0
t = 0
j = 0
pos1 = 195
pos11 = 440
pos2 = 205
pos22 = 440
p = 195
p2 = 450
pos4 = 205
pos44 = 450

pes1 = 150
pes11 = 440
pes2 = 160
pes22 = 440
pe = 150
pe2 = 450
pes4 = 160
pes44 = 450
run = True

while run:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            run = False
            sys.exit()
            print(run)
            win = pygame.display.set_mode((-30, -30))
    pygame.display.flip()
    pygame.time.delay(60)
    win.fill(0)
    t1 = pygame.Surface((10, 10))
    t1.fill((100, 0, 200))
    t2 = pygame.Surface((10, 10))
    t2.fill((0, 0, 255))
    t3 = pygame.Surface((10, 10))
    t3.fill((0, 255, 255 ))
    tt = pygame.Surface((10, 10))
    tt.fill((0, 255, 0))
    t4 = pygame.Surface((10, 10))
    t4.fill((255, 100, 0))
    t5 = pygame.Surface((10, 10))
    t5.fill((200, 100, 0))
    t6 = pygame.Surface((10, 10))
    t6.fill((255, 0, 0))
    win.blit(t1, (470, 350))
    win.blit(t2, (470, 340))
    win.blit(t3, (470, 330))
    win.blit(tt, (470, 320))
    win.blit(t4, (470, 310))
    win.blit(t5, (470, 300))
    win.blit(t6, (470, 290))
    if t < 0:
        t = 0
    if j >= 0:
        j = 0
    if t > 7:
        t = 8
    if j <= -58:
        j += 3

    pygame.draw.polygon(win, (255,0,0), ((461, 350 + j), (465, 355 + j), (461, 360 + j)), 0)
    pygame.draw.rect(win, (174, 160, 170), (460, 281, 11, 3) )
    pygame.draw.rect(win, (174, 160, 170), (464, 278, 3, 10))
    pygame.draw.rect(win, (174, 160, 170), (460, 370, 11, 3))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP_ENTER]:
        pos1 = 195
        pos11 = 440
        pos2 = 205
        pos22 = 440
        p = 195
        p2 = 450
        pos4 = 205
        pos44 = 450

        pes1 = 150
        pes11 = 440
        pes2 = 160
        pes22 = 440
        pe = 150
        pe2 = 450
        pes4 = 160
        pes44 = 450

    if t == 0:
        mov = mev = randint(-1, 1)
        mov1 = mev1 = randint(-1, 1)
        if p > 195 :
            mov -= 2
        if p < 195:
            mov += 2
        if p2 < 420 :
            mov1 += 2

        if pe > 150 :
            mev -= 2
        if pe < 150:
            mev += 2
        if pe2 < 420 :
            mev1 += 2


    if t == 1:
        mov = mev =randint(-2, 2)
        mov1 = mev1 =randint(-2, 2)
    if t == 2:
        mov = mev =randint(-3, 3)
        mov1 = mev1 = randint(-3, 3)

    if t == 3:
        mov = mev = randint(-5, 5)
        mov1 = mev1 =randint(-5, 5)

    if t == 4:
        mov = randint(-6, 6)
        mov1 = randint(-6, 6)
        mev = randint(-6, 6)
        mev1 = randint(-6, 6)
    if t == 5:
        if e1[0] < 490 and e1[0] > 10:
            mov = randint(-8, 8)
        if e1[1] < 490 and e1[1] > 10:
            mov1 = randint(-8, 7)
        if el1[0] < 490 and el1[0] > 10:
            mev = randint(-8, 8)
        if el1[1] < 490 and el1[1] > 10:
            mev1 = randint(-8, 7)
    if t == 6:
        if e1[0] < 490 and e1[0] > 10:
            mov = randint(-10, 10)
        if e1[1] < 490 and e1[1] > 10:
            mov1 = randint(-10, 9)
        if el1[0] < 490 and el1[0] > 10:
            mev = randint(-10, 10)
        if el1[1] < 490 and e1[1] > 10:
            mev1 = randint(-10, 9)
    if t == 7:
        if e1[0] < 490 and e1[0] > 10:
            mov = randint(-12, 12)
        if e1[1] < 490 and e1[1] > 10:
            mov1 = randint(-12, 11)
        if el1[0] < 490 and el1[0] > 10:
            mev = randint(-12, 12)
        if el1[1] < 490 and el1[1] > 10:
            mev1 = randint(-12, 11)
    if t > 7:
        if e1[0] < 490 and e1[0] > 10:
            mov = randint(-17, 17)
        if e1[1] < 490 and e1[1] > 10:
            mov1 = randint(-17,16)
        if el1[0] < 490 and el1[0] > 10:
            mev = randint(-17, 17)
        if el1[1] < 490 and e1[1] > 10:
            mev1 = randint(-17, 16)


    if keys[pygame.K_UP] :
        t += 1
        j -= 3
    if keys[pygame.K_DOWN] :
        t -= 1
        j += 3
    pos1 += mov
    pos11 += mov1
    pos2 += mov
    pos22 += mov1
    pos4 += mov
    pos44 += mov1
    p += mov
    p2 += mov1

    pes1 += mev
    pes11 += mev1
    pes2 += mev
    pes22 += mev1
    pes4 += mev
    pes44 += mev1
    pe += mev
    pe2 += mev1
    if a == 0:
        e1 = (p-20, p2)
        e2 = (p + 28, p2)
    if a == 2:
        e1 = (p + 5, p2 - 28)
        e2 = (p , p2 + 20)
    if a == 1:
        e1 = (p - 13, p2- 14)
        e2 = (p + 17, p2 + 14)
    if a == 3:
        e1 = (p + 23, p2- 14)
        e2 = (p - 13, p2 +14)
    if a == 4:
        e1 = (p + 28, p2)
        e2 = (p-20, p2)
    if a == 5:
        e1 = (p + 17, p2 + 14)
        e2 = (p - 13, p2- 14)
    if a == 6:
        e1 = (p, p2 + 20)
        e2 = (p + 5, p2 - 28)
    if a == 7:
        e1 = (p - 13, p2 +14)
        e2 = (p + 23, p2- 14)

    if a == 0:
        el1 = (pe-20, pe2)
        el2 = (pe + 28, pe2)
    if a == 2:
        el1 = (pe + 5, pe2 - 28)
        el2 = (pe , pe2 + 20)
    if a == 1:
        el1 = (pe - 13, pe2- 14)
        el2 = (pe + 17, pe2 + 14)
    if a == 3:
        el1 = (pe + 23, pe2- 14)
        el2 = (pe - 13, pe2 +14)
    if a == 4:
        el1 = (pe + 28, pe2)
        el2 = (pe-20, pe2)
    if a == 5:
        el1 = (pe + 17, pe2 + 14)
        el2 = (pe - 13, pe2- 14)
    if a == 6:
        el1 = (pe, pe2 + 20)
        el2 = (p + 5, p2 - 28)
    if a == 7:
        e1 = (pe - 13, pe2 +14)
        el2 = (pe + 23, pe2- 14)

    if e1[0] >= 390 or e2[0] <= 390 :
        mov = -12
        if t == 7:
            mov = -40
            if t > 7:
                mov = -60
    if e1[0] <= 40 or e2[0] <= 40:
        mov1 = 20
        if t == 7:
            mov = 40
            if t > 7:
                mov = 60
    if e1[1] >= 460 or e2[1] >= 460 :
        mov1 = -20
        if t == 7:
            mov1 = -40
            if t > 7:
                mov1 = -60
    if e1[1] <= 15 or e2[1] <= 15:
        mov1 = 20
        if t == 7:
            mov1 = 40
            if t > 7:
                mov1 = 60

    if el1[0] >= 390 or el2[0] >= 390 :
        mev = -20
        if t == 7:
            mev = -40
            if t > 7:
                mev = -60
    if el1[0] <= 40 or el2[0] <= 40:
        mev1 = 20
        if t == 7:
            mev = 40
            if t > 7:
                mev = 60
    if el1[1] >= 460 or el2[1] >= 460 :
        mev1 = -20
        if t == 7:
            mev1 = -40
            if t > 7:
                mev1 = -60
    if el1[1] <= 15 or el2[1] <= 15:
        mev1 = 20
        if t == 7:
            mev1 = 40
            if t > 7:
                mev1 = 60

    if e1[0] - el1[0] <= 15 or el1[0] - e1[0] <= 15 and t >1 :
        if e1[0] > el1[0]:
            mov += 45
            mev -= 45
        else:
            mov -= 45
            mev += 45
    if e1[1] - el1[1] <= 15 or el1[1] - e1[1] <= 15 and t >1 :
        if e1[1] > el1[1]:
            mov1 += 45
            mev1 -= 45
        else:
            mov1 -= 45
            mev1 += 45
    if e2[0] - el2[0] <= 15 or el2[0] - e2[0] <= 15 and t > 1:
        if e2[0] > el2[0]:
            mov += 45
            mev -= 45
        else:
            mov -= 45
            mev += 45
    if e2[1] - el2[1] <= 15 or el2[1] - e2[1] <= 15 and t > 1:
        if e1[1] > el1[1]:
            mov1 += 45
            mev1 -= 45
        else:
            mov1 -= 45
            mev1 += 45
    if p2 >= 490:
        mov1 -= 100
    if pe2 >= 490:
        mev1 -= 100
    if p <= 10:
        mov1 += 100
    if pe <= 10:
        mev += 100
    if p2 <= 10:
        mov1 += 100
    if pe2 <= 10:
        mev1 += 100
    if p >= 490:
        mov -= 100
    if pe >= 490:
        mev -= 100

    pygame.draw.circle(win, (0, 0, 255),(pos1, pos11) , 5, 0)
    pygame.draw.circle(win, (255, 0, 0), (pos2,pos22), 5, 0)
    pygame.draw.circle(win, (255, 0, 0), (p, p2), 5, 0)
    pygame.draw.circle(win, (0, 0, 255), (pos4, pos44), 5, 0)
    pygame.draw.circle(win, (140, 140, 0), e1, 2, 0)
    pygame.draw.circle(win, (140, 140, 0), e2, 2, 0)

    pygame.draw.circle(win, (0, 0, 255), (pes1, pes11), 5, 0)
    pygame.draw.circle(win, (255, 0, 0), (pes2, pes22), 5, 0)
    pygame.draw.circle(win, (255, 0, 0), (pe, pe2), 5, 0)
    pygame.draw.circle(win, (0, 0, 255), (pes4, pes44), 5, 0)
    pygame.draw.circle(win, (140, 140, 0), el1, 2, 0)
    pygame.draw.circle(win, (140, 140, 0), el2, 2, 0)
    a += 1
    if a == 8:
        a = 0

    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
            if x <= 467 and x >= 457 and y >= 273 and y <= 287:
                t += 1
                j -= 3
            elif x >= 453 and x <= 468 and y >= 363 and y <= 377:
                t -= 1
                j += 3
            else:
                pos1 = 195
                pos11 = 440
                pos2 = 205
                pos22 = 440
                p = 195
                p2 = 450
                pos4 = 205
                pos44 = 450

                pes1 = 150
                pes11 = 440
                pes2 = 160
                pes22 = 440
                pe = 150
                pe2 = 450
                pes4 = 160
                pes44 = 450
