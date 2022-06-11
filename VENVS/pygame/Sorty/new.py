import pygame
from random import randint
# from pygame.locals import *

width = 1000
height = 800
ilosc = 500     #max to 500 wartosci. pozniej maja <1px i nie wyswietlaja
#               COLORS
default_color = (255, 255, 255)
comp_color = (255, 0, 0)
exch_color = (0, 255, 0)
#               PYGAME THING
pygame.init()
refresh = pygame.USEREVENT + 0
change_mode = pygame.USEREVENT + 1
screen = pygame.display.set_mode((width, height))
done = False
clock = pygame.time.Clock()
smallfont = pygame.font.SysFont('Arial', 40)
Field_X = int(0.9 * width)
border_width_x = (width - Field_X) // 2
Field_Y = int(0.5 * height)
border_width_y = (height - Field_Y) // 2
center_of_y = ((Field_Y / 2) * 1.3)
end_of_usedY = height - border_width_y * 1.4
#               Napisy
T_speed = ''
T_comp = ''
T_swap = ''
T_method = ''
T_state = ''
#               SETTING UP DATA
liczby = []
obiekty = []

#                Generating random numbers and getting Max value of random numbers
for _ in range(ilosc):
    liczby.append(randint(-ilosc // 2, ilosc // 2))
extremum = max(max(liczby), abs(min(liczby)))
multipicator = center_of_y // extremum
kopia = liczby


def configure():
    global width_of_obj
    width_of_obj = Field_X / ilosc
    global obiekty
    global object_colors
    [obiekty.append((width_of_obj, abs(liczba) * multipicator)) for liczba in liczby]
    Starting_X_pos = border_width_x
    for poz, ob_li in enumerate(zip(obiekty, liczby)):
        obiekt, liczba = ob_li
        pos_y = center_of_y if liczba < 0 else center_of_y - obiekt[1]
        obiekty[poz] = pygame.Rect(Starting_X_pos, pos_y, obiekt[0], obiekt[1])
        Starting_X_pos += width_of_obj
    object_colors = [default_color for _ in obiekty]


def generator_sortow(start_pos=None):
    keys = ['Bubble-Max',
            'Bubble-Min',
            'Insert-Max',
            'Insert-Min',
            'QuickSort-Max']
    generatory_sortow = {
        'Bubble-Max': bubble_sort(liczby, po_czym='MAX'),
        'Bubble-Min': bubble_sort(liczby, po_czym='MIN'),
        'Insert-Max': insertionSort(liczby),
        'Insert-Min': insertionSort(liczby, po_czym='MIN'),
        'QuickSort-Max': quickSort(liczby)
    }
    i = 0
    m = len(keys) - 1
    for pos in keys:
        if pos == start_pos:
            break
        i += 1
    while True:
        if i > m:
            i = 0
        yield (generatory_sortow.get(keys[i]), keys[i])
        i += 1


def bubble_sort(tabela, po_czym='MAX'):
    n = len(tabela) - 1
    global comp
    global swp
    swap = False
    for i in range(n):
        for j in range(n - i):
            comp += 1
            yield (j, j + 1, 0)
            if po_czym == 'MAX':
                if tabela[j] > tabela[j + 1]:
                    swap = True
            else:
                if tabela[j] < tabela[j + 1]:
                    swap = True

            if swap:
                tabela[j], tabela[j + 1] = tabela[j + 1], tabela[j]
                swap = False
                swp += 1
                yield (j, j + 1, 1)


def insertionSort(arr, po_czym='MAX'):
    global swp
    global comp

    def compare(pos, pos2, how):
        if how == 'MAX':
            if pos < pos2:
                return True
        elif how == 'MIN':
            if pos > pos2:
                return True
        return False

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and compare(key, arr[j], po_czym):
            comp += 1
            yield (j, j + 1, 0)
            swp += 1
            yield (j, j + 1, 1)
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def quickSort(arr):
    global swp
    global comp
    pos = 0
    tablice = [arr]
    while any([True if len(pos) > 1 else False for pos in tablice]):
        n = len(tablice[pos]) - 1
        obiektow_do_poz = sum([1 for sublist in tablice[:pos] for liczba in sublist])
        if n + 1 < 2:
            pos += 1
            continue
        pivot = n
        i = -1
        j = -1
        while True:
            i += 1
            j += 1
            # print('C', obiektow_do_poz + i, obiektow_do_poz + pivot)
            comp += 1
            yield (obiektow_do_poz + i, obiektow_do_poz + pivot, 0)
            if i == pivot:
                # print('Z', obiektow_do_poz + i, obiektow_do_poz + pivot)
                tablice[pos][j], tablice[pos][pivot] = tablice[pos][pivot], tablice[pos][j]
                swp += 1
                yield (obiektow_do_poz + j, obiektow_do_poz + pivot, 1)
                pivot = j
                tablice.insert(pos, tablice[pos][0:pivot])
                pos += 1
                tablice.insert(pos + 1, tablice[pos][pivot + 1:n + 1])
                tablice[pos] = [tablice[pos][pivot]]
                pos = 0
                break
            if tablice[pos][i] <= tablice[pos][pivot]:
                # print('Z', obiektow_do_poz + i, obiektow_do_poz + j)
                swp += 1
                yield (obiektow_do_poz + i, obiektow_do_poz + j, 1)
                tablice[pos][i], tablice[pos][j] = tablice[pos][j], tablice[pos][i]
            else:
                j -= 1
    # flattened = [liczba for sublist in tablice for liczba in sublist]
    # print(flattened)


def draw():
    CMaxY = 0
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, height))
    pygame.draw.line(screen, default_color, (border_width_x, center_of_y),
                     (width - border_width_x, center_of_y))
    pygame.draw.line(screen, default_color,
                     (0, end_of_usedY),
                     (width, end_of_usedY))
    #   Time Button
    pygame.draw.rect(screen, (default_color),
                     (0.01 * width, end_of_usedY + 0.03 * height,
                      145, 50))
    screen.blit(T_speed, (0.015 * width, end_of_usedY + 0.03 * height))
    #   Method Button
    pygame.draw.rect(screen, (default_color),
                     (0.01 * width + 155, end_of_usedY + 0.03 * height,
                      395, 50))
    screen.blit(T_method, (0.015 * width + 155, end_of_usedY + 0.03 * height))
    #   Change State Button
    pygame.draw.rect(screen, (default_color),
                     (0.01 * width + 560, end_of_usedY + 0.03 * height,
                      80, 50))
    screen.blit(T_state, (0.015 * width + 565, end_of_usedY + 0.03 * height))
    CMaxY += end_of_usedY + 0.03 * height + 50
    #   Comp Button
    pygame.draw.rect(screen, (default_color),
                     (0.01 * width, CMaxY + 0.01 * height,
                     510, 50))
    screen.blit(T_comp, (0.015 * width, CMaxY + 0.01 * height))
    CMaxY += 60
    #   Insert Button
    pygame.draw.rect(screen, (default_color),
                     (0.01 * width, CMaxY + 0.01 * height,
                     510, 50))
    screen.blit(T_swap, (0.015 * width, CMaxY + 0.01 * height))
    # print(pygame.font.Font.size(smallfont,'Play'))
    for obj, color in zip(obiekty, object_colors):
        pygame.draw.rect(screen, color, obj)


def napisy():
    global T_comp, T_method, T_swap, T_speed, T_state
    T_speed = smallfont.render(f'speed : {speed}', True, (0, 0, 0))
    T_comp = smallfont.render(f'Comp: {comp}', True, (0, 0, 0))
    T_swap = smallfont.render(f'Swap: {swp}', True, (0, 0, 0))
    T_method = smallfont.render(f'Method: {nazwa_gen}', True, (0, 0, 0))
    T_state = smallfont.render(f'{is_running}', True, (0, 0, 0))


def match_button(_type):
    if _type == 'time':
        if 0.01 * width <= mouse[0] <= 0.01 * width + 145 and\
                end_of_usedY + 0.03 * height <= mouse[1] <= end_of_usedY + 0.03 * height + 50:
            return True
    elif _type == 'method':
        if 0.01 * width + 60 <= mouse[0] <= 0.7 * width and\
                end_of_usedY + 0.03 * height <= mouse[1] <= end_of_usedY + 0.03 * height + 50:
            return True
    elif _type == 'changeState':
        if 0.7 * width + 10 <= mouse[0] <= 0.7 * width + 80 and\
                end_of_usedY + 0.03 * height <= mouse[1] <= end_of_usedY + 0.03 * height + 50:
            return True
    return False


def render_comparisons():
    global object_colors
    global continue_iter
    global end_pos
    try:
        ruch = next(generator)
    except StopIteration:
        ruch = (-1, -1, -1)
    if ruch[2] == -1:
        if end_pos < end_max:
            object_colors[end_pos] = exch_color
        else:
            continue_iter = False
        end_pos += 1
    elif ruch[2] == 0:
        object_colors = [default_color for _ in range(len(object_colors))]
        object_colors[ruch[0]] = comp_color
        object_colors[ruch[1]] = comp_color
    elif ruch[2] == 1:
        temp = obiekty[ruch[0]]
        obiekty[ruch[0]] = pygame.Rect(
            obiekty[ruch[1]].left,
            obiekty[ruch[0]].top,
            obiekty[ruch[0]].width,
            obiekty[ruch[0]].height)
        obiekty[ruch[1]] = pygame.Rect(
            temp.left,
            obiekty[ruch[1]].top,
            obiekty[ruch[1]].width,
            obiekty[ruch[1]].height)
        obiekty[ruch[0]], obiekty[ruch[1]] = obiekty[ruch[1]], obiekty[ruch[0]]
        object_colors = [default_color for _ in object_colors]
        object_colors[ruch[0]] = exch_color
        object_colors[ruch[1]] = exch_color


configure()
continue_iter = True
sort_gen = generator_sortow()
generator, nazwa_gen = next(sort_gen)
comp = 0
swp = 0
speed = 1
pygame.time.set_timer(refresh, int(1000 / pow(2, speed)))
end_pos = 0
end_max = len(object_colors)
state = False
allowed = True
is_running = 'Stop' if state is True else 'Play'

while not done:
    mouse = pygame.mouse.get_pos()
    napisy()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if match_button('time'):
                speed += 1
                if speed == 10:
                    speed = 1
            elif match_button('method') and allowed is True and state is not True:
                allowed = False
                end_pos = 0
                continue_iter = True
                sort_gen.close()
                del sort_gen
                comp = 0
                swp = 0
                sort_gen = generator_sortow(start_pos=nazwa_gen)
                next(sort_gen)
                generator, nazwa_gen = next(sort_gen)
                pygame.time.set_timer(change_mode, 10)
            elif match_button('changeState'):
                state = not state
                is_running = 'Stop' if state is True else 'Play'
        elif event.type == refresh and state is True:
            if continue_iter:
                render_comparisons()
                # moze przeniesc timer do ifa i zmienic warunek na if not
            pygame.time.set_timer(refresh, int(1000 / pow(2, speed)))
        elif event.type == change_mode:
            allowed = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state = not state
                is_running = 'Stop' if state is True else 'Play'



    if not continue_iter:
        continue
    draw()
    pygame.display.flip()









