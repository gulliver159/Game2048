# Вывод главного меню, на котором осуществляется выбор режима игры, размера поля и возможность загрузить сохранение
# При выборе новой игры начинается основной цикл игры
# При выборе режима случайного поля рандомно находиться максимальное значение, которое должно быть на поле и запускается алгоритм игры без участия игрока
# Затем передается управление игрока с полученным полем и счетом
# При выборе загрузки сохранения открывается новое окно, в котором пользователь вводит свой ник, который и является названием файла, в котором находится сохранение
# Затем передается управление игроку с считанным счетом и полем
# Выйти из цикла игры возможно разными способами, выйгрышем, проигрышем и по желанию игрока
# Если игрок выйграл, то есть получил на поле значение 2048, то открывается окно с поздравлениями и возможностью ввода ника игрока для внесения его на доску почета
# Если игрок проиграл, то есть на поле больше нет пустых ячеек и нет возможности соединить какие либо ячейки, то выводится
# соответствующее окно с возможностью ввода ника игрока для внесения его на доску почета
# Если игра завершилась по желанию игрока, при нажатии клавиши ESC, то выводится окно с возможностью ввода ника игрока для внесения его на доску почета и сохранения игры
# Также присутствует обработка того, чтобы не вносить игрока на доску почета, если он начал играт с режима случайного поля

## Цикл игры:
# Ждать от пользователя команды
# Когда получим команду, обработать массив
# Найти пустые клетки
# Если есть пустые клетки, случайно выбрать одну из них и положить туда 2
# Если пустых клеток нет и нельзя двигать массив, игра закончена

from Logics import *
import sys
import pygame as pg
import random as rnd

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
    256: (255, 185, 128),
    512: (255, 185, 0),
    1024: (255, 155, 255),
    2048: (255, 155, 128)
}

# Максимальные значения, которые могут появиться на поле, при режиме случайное поле
MAX_VALUE = {
    1: 32,
    2: 64,
    3: 128,
    4: 256,
    5: 512,
    6: 1024
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
            self.TITLE_REC = pg.Rect(0, 0, self.WIDTH, 110)
            self.Shift = 0
            self.size_font_text = 70
        elif lenght_mas == 6:
            self.BLOCKS = 6
            self.SIZE_BLOCK = 70
            self.MARGIN = 10
            self.WIDTH = self.BLOCKS * self.SIZE_BLOCK + (self.BLOCKS + 1) * self.MARGIN
            self.HEIGHT = self.WIDTH + 110
            self.TITLE_REC = pg.Rect(0, 0, self.WIDTH, 110)
            self.Shift = 40
            self.size_font_text = 45


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
                text_x = w + (prs.SIZE_BLOCK - font_w) / 2 + 2
                text_y = h + (prs.SIZE_BLOCK - font_h) / 2 + 2
                screen.blit(text, (text_x, text_y))


# Отрисовка верхнего бара
def draw_bar(score, prs):
    pg.draw.rect(screen, WHITE, prs.TITLE_REC)
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

    font = pg.font.SysFont("stxingkai", 50)
    text_new_game = font.render("Новая игра", True, BLACK)
    text_random = font.render("Режим случайное поле", True, BLACK)

    img2048 = pg.image.load('logo.jpg')
    while True:
        # Обработчик событий
        for event in pg.event.get():
            if event.type == pg.QUIT:  # Если пользователь нажал на выход
                pg.quit()
                sys.exit(0)  # Закрытие окошка
        screen.fill(WHITE)
        screen.blit(pg.transform.scale(img2048, [200, 200]), [10, 20])
        screen.blit(text, (230, 85))
        screen.blit(text_new_game, (157, 255))
        screen.blit(text_random, (55, 380))
        # Кнопки
        draw_button(90, 310, 110, 45, "4x4", start_game, 4)
        draw_button(300, 310, 110, 45, "6x6", start_game, 6)

        draw_button(87, 520, 325, 45, "Загрузить сохранение", enter_username)
        draw_button(90, 430, 110, 45, "4x4", start_game_bot, 4)
        draw_button(300, 430, 110, 45, "6x6", start_game_bot, 6)
        pg.display.update()


# Отрисовка кнопок
def draw_button(x, y, width, height, text_1, action, lenght=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    font = pg.font.SysFont("stxingkai", 40)
    # При наведении на кнопку мышкой
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pg.draw.rect(screen, COLOR_BUTTON_ACTIVE, (x, y, width, height))
        text = font.render(f"{text_1}", True, BLACK)
        if lenght is not None:
            screen.blit(text, (x + 32, y + 10))
        else:
            screen.blit(text, (x + 15, y + 10))
        # При клике на кнопку
        if click[0] == 1:
            if lenght is not None:
                # Создание поля
                mas = [[0 for x in range(lenght)] for x in range(lenght)]
                action(mas)
            else:
                action()
    else:
        pg.draw.rect(screen, BLACK, (x, y, width, height))
        text = font.render(f"{text_1}", True, WHITE)
        if lenght is not None:
            screen.blit(text, (x + 32, y + 10))
        else:
            screen.blit(text, (x + 15, y + 10))


# Прорисовка вывода при выйгрыше, проигрыше и окончании игры по желанию игрока
def draw_end_window(score, text_1, is_bot=False, mas=False):
    name = 'Введите имя'
    write_text_on_end_window(score, text_1, name)
    is_find_name = False
    while not is_find_name:
        # Обработчик событий
        for event in pg.event.get():
            if event.type == pg.QUIT:  # Если пользователь нажал на выход
                pg.quit()
                sys.exit(0)  # Закрытие окошка
            elif event.type == pg.KEYDOWN:
                # Ввод имени игрока
                if event.unicode.isalpha():
                    if name == 'Введите имя':
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pg.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pg.K_RETURN:
                    if len(name) > 1:
                        global username
                        username = name
                        is_find_name = True
                        break

        write_text_on_end_window(score, text_1, name)

    if mas != False:
        save_game(score, mas)  # Сохранение игры в файл
    if not is_bot:
        write_on_honor_board()  # Запись результата на доску почета

    pg.quit()
    sys.exit(0)  # Закрытие окошка


# Вывод текста в окне конца игры
def write_text_on_end_window(score, text_1, name):
    # Вывод вообщения
    screen.fill(WHITE)
    font = pg.font.SysFont("simsun", 70)
    text = font.render(f"{text_1}", True, BLACK)
    rect_text = text.get_rect()
    rect_text.center = screen.get_rect().center
    screen.blit(text, (rect_text[0], 120))
    # Вывод счета
    font_score = pg.font.SysFont("simsun", 50)
    text_score = font_score.render(f"Ваш счет: {score}", True, BLACK)
    rect_text_score = text_score.get_rect()
    rect_text_score.center = screen.get_rect().center
    screen.blit(text_score, (rect_text_score[0], 220))
    # Ввод имени игрока
    font_name = pg.font.SysFont("simsun", 50)
    text_name = font_name.render(name, True, BLACK)
    rect_text_name = text_name.get_rect()
    rect_text_name.center = screen.get_rect().center
    screen.blit(text_name, (rect_text_name[0], 350))
    pg.display.update()


# Сохранение игры в файл
def save_game(score, mas):
    global username
    name_file = username
    name_file += ".txt"
    with open(name_file, 'tw', encoding='utf-8') as f:
        # Вывод счета
        f.write(str(score) + "\n")
        # Вывод режима игры (4х4, 6х6)
        f.write(str(len(mas)) + "\n")
        for row in mas:
            for i in row:
                f.write(str(i) + "\n")
    print(name_file)


# Считывание игры из файла
def read_game():
    global username
    name_file = username
    name_file += ".txt"
    with open(name_file) as f:
        # Ввод счета
        global score
        score = int(f.readline())
        # Ввод режима игры (4х4, 6х6)
        lenght_mas = int(f.readline())
        # Создание поля
        mas = [[0 for x in range(lenght_mas)] for x in range(lenght_mas)]
        for i in range(lenght_mas):
            for j in range(lenght_mas):
                mas[i][j] = int(f.readline())

    start_game(mas)


# Добавление игрока на доску почета
def write_on_honor_board():
    global username
    global score
    with open('honor_board.txt', 'a') as f:
        # Вывод имени
        f.write(username + " ")
        # Вывод счета
        f.write(str(score) + "\n")


# Ввод имени пользователя
def enter_username():
    screen.fill(WHITE)
    name = 'Введите имя'
    # Ввод имени игрока
    font_name = pg.font.SysFont("simsun", 50)
    text_name = font_name.render(name, True, BLACK)
    rect_text_name = text_name.get_rect()
    rect_text_name.center = screen.get_rect().center
    screen.blit(text_name, (rect_text_name[0], 100))
    pg.display.update()

    is_find_name = False
    while not is_find_name:
        # Обработчик событий
        for event in pg.event.get():
            if event.type == pg.QUIT:  # Если пользователь нажал на выход
                pg.quit()
                sys.exit(0)  # Закрытие окошка
            elif event.type == pg.KEYDOWN:
                # Ввод имени игрока
                if event.unicode.isalpha():
                    if name == 'Введите имя':
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pg.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pg.K_RETURN:
                    if len(name) > 2:
                        global username
                        username = name
                        is_find_name = True
                        break
        screen.fill(WHITE)
        text_name = font_name.render(name, True, BLACK)
        rect_text_name = text_name.get_rect()
        rect_text_name.center = screen.get_rect().center
        screen.blit(text_name, (rect_text_name[0], 150))
        pg.display.update()

    read_game()


# Режим случайное поле
def start_game_bot(mas, max_value=None):
    is_bot = True
    lenght_mas = len(mas)
    prs = Parametrs(lenght_mas)

    # Проставляем первые две двойки на поле
    set_2(mas)
    set_2(mas)

    if max_value is None:
        # Рандомно выбираем максимальное число, которое будет на поле
        index_max_value = rnd.randint(1, lenght_mas)
        max_value = MAX_VALUE[index_max_value]

    global score

    is_end = False
    ## Цикл игры ##
    while (is_zero_in_mas(mas) or can_move(mas)) and not is_win(mas) and not is_win_bot(mas, max_value):
        mas, score = move_left(mas, score)
        rnd_direction = rnd.randint(1, 4)
        if rnd_direction == 1:  # Если нажата кнопка - влево
            mas, score = move_left(mas, score)
        elif rnd_direction == 2:  # Если нажата кнопка - вправо
            mas, score = move_right(mas, score)
        elif rnd_direction == 3:  # Если нажата кнопка - вверх
            mas, score = move_up(mas, score)
        elif rnd_direction == 4:  # Если нажата кнопка - вниз
            mas, score = move_down(mas, score)
        if is_zero_in_mas(mas):
            set_2(mas)

    if is_win(mas):
        draw_end_window(score, "Вы выйграли!!!", is_bot)
    elif not is_zero_in_mas(mas) and not can_move(mas):
        mas_for_return = [[0 for x in range(lenght_mas)] for x in range(lenght_mas)]
        start_game_bot(mas_for_return, max_value)
    elif is_win_bot(mas, max_value):
        start_game(mas, is_bot)


# Цикл игры
def start_game(mas, is_bot=False):
    lenght_mas = len(mas)
    prs = Parametrs(lenght_mas)

    # Проставляем первые две двойки на поле
    set_2(mas)
    set_2(mas)

    global screen
    pg.draw.rect(screen, BLACK, pg.Rect(0, 0, WIDTH_INTRO, HEIGHT_INTRO))
    pg.display.set_caption("2048")

    # Отрисовываем начальное поле
    draw_field(mas, СOLORS, prs)
    global score
    draw_bar(score, prs)
    pg.display.update()

    is_end = False

    while (is_zero_in_mas(mas) or can_move(mas)) and not is_win(mas) and not is_end:
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
                    multiply_on_2(mas)
                elif event.key == pg.K_5:  # Если нажата кнопка - вниз
                    mas = multiply_on_2(mas)
                elif event.key == pg.K_ESCAPE:  # Если нажата кнопка - ESC
                    is_end = True
                else:
                    continue
                if is_zero_in_mas(mas):
                    set_2(mas)
                draw_bar(score, prs)
                draw_field(mas, СOLORS, prs)  # Перерисовываем поле
                pg.display.update()

    # Вывод окна конца игры
    while True:
        if is_win(mas):
            draw_end_window(score, "Вы выйграли!!!", is_bot)
        elif is_end:
            draw_end_window(score, "Конец игры", is_bot, mas)
        else:
            draw_end_window(score, "Вы проиграли(", is_bot)


# Значение счета игрока
score = 0
# Ник пользователя
username = None

# Предварительная отрисовка
pg.init()

# Создание окна игры
WIDTH_INTRO = 490
HEIGHT_INTRO = 600
screen = pg.display.set_mode((WIDTH_INTRO, HEIGHT_INTRO))

# Отрисовка меню
draw_intro()















