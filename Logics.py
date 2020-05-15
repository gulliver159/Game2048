import random as rnd
import numpy as np


# region main logic
# Вывод массива
def pretty_print(mas):
    print("-" * 10)
    for row in mas:
        print(*row)


def set_2(mas):
    # input()
    Empty = get_empty_list(mas)  # Получаем порядковые номера всех пустых ячеек
    rnd.shuffle(Empty)  # Мешаем их
    rnd_num = Empty.pop()  # Достаем последнее из списка пустых ячеек
    x, y = get_index_from_number(mas, rnd_num)
    mas[x][y] = 2  # Ставим на это место двойку
    pretty_print(mas)


# Возвращает порядковые номера всех пустых клеток поля
def get_empty_list(mas):
    lenght_mas = len(mas[0])
    Empty = []
    for i in range(lenght_mas):
        for j in range(lenght_mas):
            if mas[i][j] == 0:
                Empty.append(get_number_from_index(mas, i, j))
    return Empty


# Проверяет, есть ли на поле пустые ячейки
def is_zero_in_mas(mas):
    for row in mas:
        if 0 in row:
            return True
    return False


# Возвращает порядковый номер ячейки поля
def get_number_from_index(mas, i, j):
    return i * len(mas[0]) + j + 1


# Возвращает номер строки и столбца ячейки поля по ее порядковому номеру
def get_index_from_number(mas, num):
    lenght_mas = len(mas[0])
    num -= 1
    x, y = num // lenght_mas, num % lenght_mas
    return x, y


# endregion

## Реализация перемещения ячеек по логике игры ##
# region moving
# При свайпе влево
def move_left(mas, score):
    lenght_mas = len(mas[0])
    for row in mas:
        while 0 in row:
            row.remove(0)  # Удаляем все нули на поле
        while len(row) != lenght_mas:
            row.append(0)  # Добавляем недостающие ячейки
    # Сложение чисел
    for i in range(lenght_mas):
        for j in range(lenght_mas - 1):  # Идем по столбцам слево направо
            # Если числа стоят рядом, то правое умножаем на два, а левое удаляем
            if mas[i][j] == mas[i][j + 1] and mas[i][j] != 0:
                mas[i][j] *= 2
                score += mas[i][j]
                mas[i].pop(j + 1)
                mas[i].append(0)  # Добавляем недостающие ячейки
    return mas, score


# При свайпе вправо
def move_right(mas, score):
    lenght_mas = len(mas[0])
    for row in mas:
        while 0 in row:
            row.remove(0)  # Удаляем все нули на поле
        while len(row) != lenght_mas:
            row.insert(0, 0)  # Добавляем недостающие ячейки
    # Сложение чисел
    for i in range(lenght_mas):
        for j in range(lenght_mas - 1, 0, -1):  # Идем по столбцам справо налево
            # Если числа стоят рядом, то правое умножаем на два, а левое удаляем
            if mas[i][j] == mas[i][j - 1] and mas[i][j] != 0:
                mas[i][j] *= 2
                score += mas[i][j]
                mas[i].pop(j - 1)
                mas[i].insert(0, 0)  # Добавляем недостающие ячейки
    return mas, score


# При свайпе вверх
def move_up(mas, score):
    lenght_mas = len(mas)
    for j in range(lenght_mas):
        column = []  # Будет храниться столбец массива
        for i in range(lenght_mas):
            if mas[i][j] != 0:
                column.append(mas[i][j])
        while len(column) != lenght_mas:  # Пока не подойдет размер
            column.append(0)
        # Сложение чисел
        for i in range(lenght_mas - 1):
            if column[i] == column[i + 1] and column[i] != 0:
                column[i] *= 2
                score += column[i]
                column.pop(i + 1)
                column.append(0)
        # Вставка обратно в массив
        for i in range(lenght_mas):
            mas[i][j] = column[i]
    return mas, score


# При свайпе вниз
def move_down(mas, score):
    lenght_mas = len(mas)
    for j in range(lenght_mas):
        column = []  # Будет храниться столбец массива
        for i in range(lenght_mas):
            if mas[i][j] != 0:
                column.append(mas[i][j])
        while len(column) != lenght_mas:  # Пока не подойдет размер
            column.insert(0, 0)
        # Сложение чисел
        for i in range(lenght_mas - 1, 0, -1):
            if column[i] == column[i - 1] and column[i] != 0:
                column[i] *= 2
                score += column[i]
                column.pop(i - 1)
                column.insert(0, 0)
        # Вставка обратно в массив
        for i in range(lenght_mas):
            mas[i][j] = column[i]
    return mas, score


# endregion

# Проверка на того, сможет ли пользователь свайпнуть в какую либо сторону
def can_move(mas):
    lenght_mas = len(mas)
    for i in range(lenght_mas - 1):
        for j in range(lenght_mas - 1):
            if mas[i][j] == mas[i][j + 1] or mas[i][j] == mas[i + 1][j]:
                return True
    return False


# Проверка на окончания игры (выйгрыш)
def is_win(mas):
    for row in mas:
        for i in row:
            if i == 64:
                return True
    return False
