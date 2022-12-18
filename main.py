import math
from math import pi
import pygame.gfxdraw
from Map_Zone_Text import Map, Zone, M, N

pygame.init()


def leng(f, g):
    return math.sqrt((f[0] - g[0]) ** 2 + (f[1] - g[1]) ** 2)


sc = pygame.display.set_mode((M, N))

pygame.display.set_caption('This is fine !')

clock = pygame.time.Clock()

FPS = 60
sc.fill((0, 0, 0))
flend = True
(x, y) = (760, 380)

an = 0
focus = 1
fd = 101
pause = 1
begin = True
trap = False
deadfisttime = True
isdead = False
paradox = False
motionblock = True
dead_body = dict()
countdeadfisttime = 0
countparaox = 0
bodycount = 0
(z, t) = (x + 20, y)
(a, b) = (1, 0)
background = pygame.Surface((M, N))
front = pygame.Surface((M, N))
bounds = pygame.Surface((M, N))

room2 = False
room3 = False
while flend:
    if pause:
        pygame.mouse.set_visible(False)
    else:
        pygame.mouse.set_visible(True)

    keys = pygame.key.get_pressed()
    sc.fill((30, 30, 30))
    sc.blit(Map, (0, 0))

    for i in range(fd):
        pygame.draw.arc(background, (30, 30, 30), (x - i, y - i, 2 * i, 2 * i),
                        (-pi / 3) / focus - an, (pi / 3) / focus - an)
        pygame.draw.arc(front, (30, 30, 30), (x - i, y - i, 2 * i, 2 * i),
                        (-pi / 3) / focus - an, (pi / 3) / focus - an)
    background.set_colorkey((30, 30, 30))
    front.set_colorkey((30, 30, 30))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            flend = False
        if focus <= 4 and not pause:
            if event.type == pygame.MOUSEMOTION:
                (z, t) = event.pos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if paradox and countparaox <= 7:
                    countparaox += 1
                elif paradox:
                    pygame.quit()
                if deadfisttime and isdead:
                    countdeadfisttime += 1
                elif isdead:
                    isdead = False

                begin = False
                if pause and not isdead:
                    pause = 0

                    pygame.mouse.set_pos([z, t])
                else:
                    pause = 1

        if event.type == pygame.MOUSEMOTION:
            (a, b) = (z - x, t - y)

        if tuple(Zone.get_at((x, y))) == (255, 100, 255, 255) and a >= 0 and not trap:
            pause = True
            trap = True


        elif (tuple(Zone.get_at((x, y))) == (255, 0, 255, 255) or tuple(Zone.get_at((x, y))) == (
                255, 100, 255, 255)) and not a >= 0 and trap:
            pygame.draw.rect(Zone, (0, 100, 0), (x - 2, y - 2, 4, 4))
            pygame.draw.rect(Map, (0, 100, 0), (x - 2, y - 2, 4, 4))
            dead_body[bodycount] = (x, y)
            bodycount += 1
            (x, y) = (M // 2, N // 2)
            trap = False
            isdead = True
    if focus <= 4 and not pause and not motionblock:
        if keys[pygame.K_d] and tuple(Zone.get_at((x + 2, y))) != (255, 0, 0, 255):
            x += 1
        if keys[pygame.K_a] and tuple(Zone.get_at((x - 2, y))) != (255, 0, 0, 255):
            x -= 1
        if keys[pygame.K_w] and tuple(Zone.get_at((x, y - 2))) != (255, 0, 0, 255):
            y -= 1
        if keys[pygame.K_s] and tuple(Zone.get_at((x, y + 2))) != (255, 0, 0, 255):
            y += 1
    if keys[pygame.K_q]:
        if focus < 100:
            focus *= 1.1
    if not keys[pygame.K_q]:
        if focus > 1:
            focus /= 1.1
        else:
            focus = 1

    an = math.atan2(t - y, z - x)
    if focus <= 21:
        fd = round(101 + 5 * focus - 5)
    else:
        fd = 201
    for i in range(fd):
        if focus < 4:
            pygame.draw.arc(front, (230 - 2 * i, 230 - 2 * i, 230 - 2 * i), (x - i, y - i, 2 * i, 2 * i),
                            (-pi / 3) / focus - an, (pi / 3) / focus - an)
        elif focus <= 10:
            pygame.draw.arc(front, (round(230 - 1.5 * i), round(230 - 1.5 * i), round(230 - 1.5 * i)),
                            (x - i, y - i, 2 * i, 2 * i),
                            (-pi / 3) / focus - an, (pi / 3) / focus - an)
        else:
            pygame.draw.arc(front, (230, 255 - 11 * min(focus, 21), 255 - 11 * min(focus, 21)),
                            (x - i, y - i, 2 * i, 2 * i),
                            (-pi / 3) / focus - an, (pi / 3) / focus - an)
    for i in range(bodycount):
        if focus <= 4 and leng(dead_body[i], (x, y)) <= 100 and pi / 6 / focus <= math.atan2(
                math.cos(an) * (dead_body[i][0] - x) + math.sin(an) * (dead_body[i][1] - y),
                math.sin(an) * (dead_body[i][0] - x) - math.cos(an) * (
                        dead_body[i][1] - y)) <= 5 * pi / 6 / focus:
            paradox = True

    sc.blit(background, (0, 0))
    front.set_alpha(100)
    sc.blit(front, (0, 0))

    bounds.fill((0, 0, 0))
    pygame.gfxdraw.box(bounds, (660, 330, 200, 250), (30, 30, 30))
    if room2:
        pygame.gfxdraw.box(bounds, (48, 240, M - 100 + 4, 92), (30, 30, 30))
    else:
        pygame.gfxdraw.box(background, (48, 240, M - 100 + 4, 90), (0, 0, 0))
        pygame.gfxdraw.box(background, (48, 330, 660 - 48, 2), (0, 0, 0))
        pygame.gfxdraw.box(background, (860, 330, M - 52 - 860 + 4, 2), (0, 0, 0))

    bounds.set_colorkey((30, 30, 30))
    sc.blit(bounds, (0, 0))

    if begin:
        from Map_Zone_Text import Text0

        sc.blit(Text0.serf, Text0.serf.get_rect(center=(M // 2, N // 2)))
    elif pause and tuple(Zone.get_at((x, y))) == (0, 0, 255, 255):
        from Map_Zone_Text import Text1

        sc.blit(Text1.serf, Text1.serf.get_rect(center=(M // 2, N // 2)))
        motionblock = False
    elif pause and tuple(Zone.get_at((x, y))) == (0, 0, 254, 255):
        room2 = True
        pygame.gfxdraw.box(Zone, (740, 330, 40, 2), (0, 255, 0))
        pygame.gfxdraw.box(Map, (740, 330, 40, 2), (0, 255, 0))
        from Map_Zone_Text import Text2

        sc.blit(Text2.serf, Text2.serf.get_rect(center=(M // 2, N // 2)))
    elif trap:
        from Map_Zone_Text import Text3

        sc.blit(Text3.serf, Text3.serf.get_rect(center=(M // 2, N // 2)))
    elif isdead and deadfisttime:
        sc.fill((0, 0, 0))
        if countdeadfisttime <= 3:
            from Map_Zone_Text import Text4

            sc.blit(Text4[countdeadfisttime].serf, Text4[countdeadfisttime].serf.get_rect(center=(M // 2, N // 2)))
        elif countdeadfisttime == 4:
            deadfisttime = False
    elif isdead:
        pause = True

        from Map_Zone_Text import Text5

        sc.blit(Text5.serf, Text5.serf.get_rect(center=(M // 2, N // 2)))
    elif paradox:
        pause = True
        from Map_Zone_Text import Text6

        sc.blit(Text6[countparaox].serf, Text6[countparaox].serf.get_rect(center=(M // 2, N // 2)))

    pygame.display.update()
    clock.tick(FPS)
