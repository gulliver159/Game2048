import random as rnd

# Цикл игры:
# Ждать от пользователя команды
# Когда получим команду обработать массив
# Найти пустые клетки
# Если есть пустые клетки, случайно выбрать одну из них
# И положить туда либо 2, либо 4
# Если пустых клеток нет и нельзя двигать массив, игра закончена


mas = [[0, 0, 0, 0],
       [0, 0, 0, 2],
       [2, 0, 0, 0],
       [0, 0, 0, 0]]

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
                Empty.append(get_number_from_index(i, j))
    return Empty

def insert_2(mas, x, y):
    mas[x][y] = 2
    
                
# Возвращает порядковый номер ячейки поля
def get_number_from_index(mas, i, j):
    return i * len(mas[0]) + j + 1

# Возвращает номер строки и столбца ячейки поля по ее порядковому номеру
def get_index_from_number(mas, num):
    lenght_mas = len(mas[0])
    nim -= 1
    x, y = num//lenght_mas, num % lenght_mas
    return x, y

pretty_print(mas)
print(get_empty_list(mas))