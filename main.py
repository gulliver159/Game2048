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
COLOR_BUTTON_ACTIVE = (200, 200, 200)
COLOR_BUTTON_PASSIVE = (0, 0, 0)

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


# Параметры для графики в зависимости от размера поля
class Parametrs:
    def __init__(self, lenght_mas):
        if lenght_mas == 4:
            self.BLOCKS = 4
            self.SIZE_BLOCK = 110
            self.MARGIN = 10
            self.WIDTH = self.BLOCKS * self.SIZE_BLOCK + (self.BLOCKS + 1) * self.MARGIN
            self.HEIGHT = self.WIDTH + 110
            self.TITILE_REC = pg.Rect(0, 0, self.WIDTH, 110)
            self.Shift = 0
            self.size_font_text = 70
        elif lenght_mas == 6:
            self.BLOCKS = 6
            self.SIZE_BLOCK = 70
            self.MARGIN = 10
            self.WIDTH = self.BLOCKS * self.SIZE_BLOCK + (self.BLOCKS + 1) * self.MARGIN
            self.HEIGHT = self.WIDTH + 110
            self.TITILE_REC = pg.Rect(0, 0, self.WIDTH, 110)
            self.Shift = 40
            self.size_font_text = 50


# Значение счета игрока
score = 0

WIDTH_INTRO = 490
HEIGHT_INTRO = 600
screen = pg.display.set_mode((WIDTH_INTRO, HEIGHT_INTRO))


# Отрисовка игрового поля
def draw_field(mas, COLORS, prs):
    font = pg.font.SysFont("stxingkai", prs.size_font_text)
    for row in range(prs.BLOCKS):
        for column in range(prs.BLOCKS):
            value = mas[row][column]

            # Отрисовка ячеек
            w = column * prs.SIZE_BLOCK + (column + 1) * prs.MARGIN
            h = row * prs.SIZE_BLOCK + (row + 1) * prs.MARGIN + prs.SIZE_BLOCK + prs.Shift
            pg.draw.rect(screen, COLORS[value], (w, h, prs.SIZE_BLOCK, prs.SIZE_BLOCK))

            # Отрисовка цифр
            text = font.render(f'{value}', True, BLACK)
            if value != 0:
                font_w, font_h = text.get_size()
                # Получаем коородинаты, куда затем поставим цифру
                text_x = w + (prs.SIZE_BLOCK - font_w) / 2
                text_y = h + (prs.SIZE_BLOCK - font_h) / 2
                screen.blit(text, (text_x, text_y))


# Отрисовка верхнего бара
def draw_bar(score, prs):
    pg.draw.rect(screen, WHITE, prs.TITILE_REC)
    font = pg.font.SysFont("simsun", 48)
    text = font.render("Score: ", True, COLOR_TEXT)
    text_value = font.render(f"{score} ", True, COLOR_TEXT)
    screen.blit(text, (20, 35))
    screen.blit(text_value, (150, 35))


# Отрисовка начального экрана
def draw_intro():
    pg.draw.rect(screen, WHITE, pg.Rect(0, 0, WIDTH_INTRO, HEIGHT_INTRO))
    font = pg.font.SysFont("simsun", 75)
    text = font.render("Welcome!", True, BLACK)
    img2048 = pg.image.load('logo.jpg')
    while True:
        # Обработчик событий
        for event in pg.event.get():
            if event.type == pg.QUIT:  # Если пользователь нажал на выход
                pg.quit()
                sys.exit(0)  # Закрытие окошка
        screen.blit(pg.transform.scale(img2048, [200, 200]), [10, 20])
        screen.blit(text, (230, 85))
        # Кнопки
        draw_button(90, 290, 110, 45, "4x4", start_game, 4)
        draw_button(300, 290, 110, 45, "6x6", start_game, 6)
        pg.display.update()


def draw_button(x, y, width, height, text_1, action, lenght):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    font = pg.font.SysFont("stxingkai", 40)
    # При наведении на кнопку мышкой
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pg.draw.rect(screen, COLOR_BUTTON_ACTIVE, (x, y, width, height))
        text = font.render(f"{text_1}", True, BLACK)
        screen.blit(text, (x + 32, y + 10))
        # При клике на кнопку
        if click[0] == 1:
            action(lenght)
    else:
        pg.draw.rect(screen, BLACK, (x, y, width, height))
        text = font.render(f"{text_1}", True, WHITE)
        screen.blit(text, (x + 32, y + 10))


def start_game(lenght_mas):
    prs = Parametrs(lenght_mas)
    # Создание поля
    mas = [[0 for x in range(lenght_mas)] for x in range(lenght_mas)]

    # Проставляем первые две двойки на поле
    set_2(mas)
    set_2(mas)

    global screen
    screen = pg.display.set_mode((prs.WIDTH, prs.HEIGHT))
    pg.display.set_caption("2048")

    # Отрисовываем начальное поле
    draw_field(mas, СOLORS, prs)
    global score
    draw_bar(score, prs)
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
                draw_bar(score, prs)
                draw_field(mas, СOLORS, prs)  # Перерисовываем поле
                pg.display.update()
    # =============================================================================


# Предварительная отрисовка
pg.init()

draw_intro()












