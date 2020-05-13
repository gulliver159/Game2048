from Logics import *
import sys
import numpy
import pygame as pg

## Цикл игры:
# Ждать от пользователя команды
# Когда получим команду обработать массив
# Найти пустые клетки
# Если есть пустые клетки, случайно выбрать одну из них
# И положить туда либо 2, либо 4
# Если пустых клеток нет и нельзя двигать массив, игра закончена

# Цвета для графики
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)

СOLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (255, 255, 0),
    16: (255, 235, 255),
    32: (255, 235, 128),
    64: (255, 235, 0)
}


def set_2(mas):
    # input()
    Empty = get_empty_list(mas)  # Получаем порядковые номера всех пустых ячеек
    rnd.shuffle(Empty)  # Мешаем их
    rnd_num = Empty.pop()  # Достаем последнее из списка пустых ячеек
    x, y = get_index_from_number(mas, rnd_num)
    mas[x][y] = 2  # Ставим на это место двойку
    pretty_print(mas)


# Отрисовка игрового поля
def draw_field(mas, COLORS):
    pg.draw.rect(screen, WHITE, TITILE_REC)
    font = pg.font.SysFont("stxingkai", 70)
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            value = mas[row][column]

            # Отрисовка ячеек
            w = column * SIZE_BLOCK + (column + 1) * MARGIN
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
            pg.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))

            # Отрисовка цифр
            text = font.render(f'{value}', True, BLACK)
            if value != 0:
                font_w, font_h = text.get_size()
                # Получаем коородинаты, куда затем поставим цифру
                text_x = w + (SIZE_BLOCK - font_w) / 2
                text_y = h + (SIZE_BLOCK - font_h) / 2
                screen.blit(text, (text_x, text_y))


mas = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]

# Параметры для графики
BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN
HEIGHT = WIDTH + 110
TITILE_REC = pg.Rect(0, 0, WIDTH, 110)

# Предварительная отрисовка
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("2048")

# Проставляем первые две двойки на поле
set_2(mas)
set_2(mas)

# Отрисовываем начальное поле
draw_field(mas, СOLORS)
pg.display.update()

## Цикл игры ##
# =============================================================================
while is_zero_in_mas(mas):
    # Обработчик событий
    for event in pg.event.get():
        if event.type == pg.QUIT:  # Если пользователь нажал на выход
            pg.quit()
            sys.exit(0)  # Закрытие окошка
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:  # Если нажата кнопка - влево
                mas = move_left(mas)
            elif event.key == pg.K_RIGHT:  # Если нажата кнопка - влево
                mas = move_right(mas)
            # pretty_print(mas)
            set_2(mas)
            draw_field(mas, СOLORS)  # Перерисовываем поле
            pg.display.update()
# =============================================================================

















