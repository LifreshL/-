import pygame.gfxdraw

pygame.init()
M = 1500
N = 800

Map = pygame.Surface((M, N), pygame.SRCALPHA, 32)
# bounds
pygame.gfxdraw.box(Map, (0, 0, M, N), (255, 0, 0))
pygame.gfxdraw.box(Map, (50, 50, M - 100, N - 100), (30, 30, 30))
# room1
pygame.gfxdraw.box(Map, (660, 330, 200, 250), (255, 0, 0))
pygame.gfxdraw.box(Map, (660 + 2, 330 + 2, 200 - 4, 250 - 4), (30, 30, 30))
pygame.gfxdraw.box(Map, (740, 360, 40, 40), (0, 0, 255))
pygame.gfxdraw.box(Map, (820 - 2, 540 - 2, 40, 40), (0, 0, 255))
# room2
pygame.gfxdraw.box(Map, (48, 240, M - 100 + 4, 92), (255, 0, 0))
pygame.gfxdraw.box(Map, (50, 240 + 2, M - 100, 92 - 4), (30, 30, 30))

# room3


Zone = pygame.Surface((M, N))
# bounds
pygame.gfxdraw.box(Zone, (0, 0, M, N), (255, 0, 0))
pygame.gfxdraw.box(Zone, (50, 50, M - 100, N - 100), (0, 0, 0))
# room1
pygame.gfxdraw.box(Zone, (660, 330, 200, 250), (255, 0, 0))
pygame.gfxdraw.box(Zone, (660 + 2, 330 + 2, 200 - 4, 250 - 4), (0, 0, 0))
pygame.gfxdraw.box(Zone, (740, 360, 40, 40), (0, 0, 255))
pygame.gfxdraw.box(Zone, (820 - 2, 540 - 2, 40, 40), (0, 0, 254))

# room2
pygame.gfxdraw.box(Zone, (48, 240, M - 150 + 4, 92), (255, 0, 0))
pygame.gfxdraw.box(Zone, (50, 240 + 2, M - 150, 92 - 4), (0, 0, 0))

pygame.gfxdraw.box(Zone, (50, 240 + 2, M - 150, 92 - 4), (255, 0, 255))
pygame.gfxdraw.box(Zone, (M - 145, 240 + 2, 45, 92 - 4), (255, 100, 255))

# room3
pygame.gfxdraw.circle(Zone, 100, 100, 50, (0, 0, 0))


class Text:
    def __init__(self, font, size, *massage):
        self.font = pygame.font.SysFont(font, size)
        self.serf = pygame.Surface((M, N), pygame.SRCALPHA, 32)
        a = list()
        for i in range(len(massage)):
            a.append(self.font.render(massage[i], True, (255, 255, 255), (0, 0, 0)))
        for i in range(len(massage)):
            self.serf.blit(a[i], a[i].get_rect(center=(M // 2, size // 2 + 5 + i * (size + 5))))


Text0 = Text('arial', 50, 'Опа! ЙА СНОВА ЖИВУ!', 'Надо подождать когда вернётся память...',
             'Для начала нужно научится думать.',
             'Кажется, что для этого нужно нажать E')
Text1 = Text('arial', 50, 'Отлично!', 'Как я люблю думать!', 'Осбенно учитывая, что мыслительный процесс',
             'не занимает ни секунды реального времени!', 'Теперь надо вспомнить, как двигаться.',
             'Обычно я делал это используя WASD.', 'Но для начала нужно перестать думать нажав E повторно')
Text2 = Text('arial', 50, 'Думать в некоторых местах особенно полезно!', 'Например тут, я вспомнил, что двери можно открывать.')
Text3 = Text('arial', 50, 'Обернись!')
Text4 = dict()
Text4[0] = Text('arial', 50, 'Мёртв или нет?', 'А что если подумaть?')
Text4[1] = Text('arial', 75, 'Ещё!')
Text4[2] = Text('arial', 100, 'Ещё!')
Text4[3] = Text('arial', 200, 'АХАХАХАХАХАХАХАХА', 'АХАХАХАХАХАХАХАХА', 'АХАХАХАХАХАХАХАХА', 'АХАХАХАХАХАХАХАХА',
                'АХАХАХАХАХАХАХАХА')

Text5 = Text('arial', 50, 'Как там говорили в древности?', 'Мыслишь значет существуешь!')

Text6 = dict()
Text6[0] = Text('arial', 50, 'Вы обаружили своё мертвое тело.', 'Что тут произошло?', 'Таки мёртв или нет?',
                'А что если подумaть?')
Text6[1] = Text('arial', 100, 'Мёртв или нет?')
Text6[2] = Text('arial', 100, 'Мёртв или нет?', 'Мёртв или нет?')
Text6[3] = Text('arial', 100, 'Мёртв или нет?', 'Мёртв или нет?', 'Мёртв или нет?')
Text6[4] = Text('arial', 100, 'Мёртв или нет?', 'Мёртв или нет?', 'Мёртв или нет?', 'Мёртв или нет?')
Text6[5] = Text('arial', 100, 'Мёртв или нет?', 'Мёртв или нет?', 'Мёртв или нет?', 'Мёртв или нет?', 'Мёртв или нет?')
Text6[6] = Text('arial', 100, 'Мёртв или нет?', 'Мёртв или нет?', 'Мёртв или нет?', 'Мёртв или нет?', 'Мёртв или нет?',
                'Мёртв или нет?')
Text6[7] = Text('arial', 200, 'AAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAA',
                'AAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAA')

sc2 = pygame.display.set_mode((M, N))

pygame.display.set_caption('This is fine !')

clock = pygame.time.Clock()

FPS = 60

flend = True

sc2.fill((0, 0, 0))

# while flend:
#     sc2.blit(Zone, (0, 0))
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             flend = False
#
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             print(event.pos)
#
#     pygame.display.update()
#     clock.tick(FPS)
