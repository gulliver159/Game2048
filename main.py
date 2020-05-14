from Logics import *
import sys
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
COLOR_TEXT = (255, 127, 0)

СOLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (255, 255, 0),
    16: (255, 215, 255),
    32: (255, 215, 128),
    64: (255, 215, 0),
    128: (255, 185, 255),
    264: (255, 185, 128),
}

# Значение счета игрока
score = 0

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


# Отрисовка верхнего бара
def draw_bar(score):
    pg.draw.rect(screen, WHITE, TITILE_REC)
    font = pg.font.SysFont("simsun", 48)
    text = font.render("Score: ", True, COLOR_TEXT)
    text_value = font.render(f"{score} ", True, COLOR_TEXT)
    screen.blit(text, (20, 35))
    screen.blit(text_value, (150, 35))


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
draw_bar(score)
pg.display.update()

## Цикл игры ##
# =============================================================================
while is_zero_in_mas(mas) or can_move(mas):
    # Обработчик событий
    for event in pg.event.get():
        if event.type == pg.QUIT:  # Если пользователь нажал на выход
            pg.quit()
            sys.exit(0)  # Закрытие окошка
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:  # Если нажата кнопка - влево
                mas, score = move_left(mas, score)
            elif event.key == pg.K_RIGHT:  # Если нажата кнопка - вправо
                mas, score = move_right(mas, score)
            elif event.key == pg.K_UP:  # Если нажата кнопка - вверх
                mas, score = move_up(mas, score)
            elif event.key == pg.K_DOWN:  # Если нажата кнопка - вниз
                mas, score = move_down(mas, score)
            else:
                continue
            # pretty_print(mas)
            set_2(mas)
            draw_field(mas, СOLORS)  # Перерисовываем поле
            draw_bar(score) # Перерисовываем вехний бар
            pg.display.update()
# =============================================================================















