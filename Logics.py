import random as rnd


# Вывод массива
def pretty_print(mas):
    print("-" * 10)
    for row in mas:
        print(*row)


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


## Реализация перемещения ячеек по логике игры ##
# При свайпе влево
def move_left(mas):
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
                mas[i].pop(j + 1)
                mas[i].append(0)  # Добавляем недостающие ячейки
    return mas


# При свайпе вправо
def move_right(mas):
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
                mas[i].pop(j - 1)
                mas[i].insert(0, 0)  # Добавляем недостающие ячейки
    return mas






