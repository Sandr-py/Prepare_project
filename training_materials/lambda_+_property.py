from random import randint
from functools import reduce




class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def kg(self):
        print('get_kg() called')
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            print('set_kg() called')
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')
    @kg.deleter
    def kg(self):
        del self.__kg

# _________________________________________________________________

def square(x):
    return x**2

def mul_on_two(x):
    return x*2

funcs = [square, mul_on_two]

# _________________________________________________________________

gen_list = list(randint(-10, 10) for _ in range(7))

# _________________________________________________________________

str1 = list('Python 2.0')
str2 = list('Python 3.0')

# _________________________________________________________________

keys = [i for i in range(1, 11)]
elems = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']

list1 = [randint(-100, 100) for _ in range(5)]
list2 = [randint(-100, 100) for _ in range(5)]
list3 = [randint(-100, 100) for _ in range(5)]

# _________________________________________________________________
# ________________Блок_исполнения__________________________________

a = input('Введите номер задачи для её демонстрации:\n'
              '1: Работа декоратора property\n'
              '2: Работа lambda функции map\n'
              '3: Работа lambda функции filter (max/min/equal_2)\n'
              '4: Работа lambda функции filter (Поиск общих символов в 2 строках)\n'
              '5: Работа lambda функции reduce\n'
              '6: Работа lambda функции zip\n\n'
          ': ')

while type(a) != int:
    try:
        a = int(a)

        if a <= 0 or a >= 7:
            print('Неободимо ввести число-номер одной из представленных задач')
            a = input('Введите номер задачи для её демонстрации:\n'
                      '1: Работа декоратора property\n'
                      '2: Работа lambda функции map\n'
                      '3: Работа lambda функции filter (max/min/equal_2)\n'
                      '4: Работа lambda функции filter (Поиск общих символов в 2 строках)\n'
                      '5: Работа lambda функции reduce\n'
                      '6: Работа lambda функции zip\n\n'
                      ': ')
            continue

    except ValueError:
        print('Вы должны ввести интересующего задания\n\n')
        a = input('Введите номер задачи для её демонстрации:\n'
                  '1: Работа декоратора property\n'
                  '2: Работа lambda функции map\n'
                  '3: Работа lambda функции filter (max/min/equal_2)\n'
                  '4: Работа lambda функции filter (Поиск общих символов в 2 строках)\n'
                  '5: Работа lambda функции reduce\n'
                  '6: Работа lambda функции zip\n\n'
                  ': ')


if a == 1:
    p1 = KgToPounds(5)
    print(p1.kg)
    p1.kg = 10
    print(p1.kg)


elif a == 2:
    for i in range(5):
        my_list = list(map(lambda x: x(i), funcs))
        print(my_list)



elif a == 3:
    print(f"Начальный список:  {gen_list}")
    print(f"Больше нуля: {list(filter(lambda x: x >= 0, gen_list))}")
    print(f"Чётные: {list(filter(lambda x: x % 2 == 0, gen_list))}\n\n")


elif a == 4:
    print(str1, str2, sep='\n')
    repeated = list(filter(lambda x: x in str1, str2))
    print(*repeated, end='\n')


elif a == 5:
    max = reduce(lambda x, y: x if x > y else y, gen_list)
    min = reduce(lambda x, y: x if x < y else y, gen_list)
    multiply = reduce(lambda x, y: x * y, gen_list)
    print(max, min, multiply, sep='\n')


elif a == 6:
    print(f"Словарь из двух списков {dict(zip(keys, elems))}")
    print(f"Многомерный массив (матрица)")
    for i in list(zip(list1, list2, list3)):
        print(i)
