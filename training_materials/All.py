from math import sqrt
# Множественное наследование.

class Scientist:
    def __init__(self):
        print('Я учёный')


class Builder:
    def __init__(self):
        print('Я строитель')


class Person(Scientist, Builder):
    def __init__(self):
        super().__init__()
        Builder.__init__(self)
        print('Я человек')


per1 = Person()
print(Person.__mro__)

"""Создание менеджера контекста:
    Реализую работу со списком с использованием менеджера контекста.
"""

class summary():
    def __init__(self, v):
        self.v = v

    def __enter__(self):
        self.__lister = self.v[:]
        return self.__lister

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.v[:] = self.__lister
        return False


v1 = [1, 2, 3, 4]
v2 = [2, 3, 4, 5]

with summary(v1) as list:
    try:
        for i in range(len(v1)):
            list[i] += v2[i]
    except Exception as e:
        print(e)

print(v1)

"""Использование декоратора property"""
class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def kg(self):
        print(f'Получены килограммы {self.__kg}')
        return self.__kg


    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
            print('Килограммы изменены')
        else:
            raise ValueError('Килограммы задаются только числами')

ghgh = KgToPounds(10)
print(ghgh.kg)
ghgh.kg = 5
print(ghgh.kg)

"""Написание собственного декоратора"""

def Triangle(func):
    def Wrapper(*args):
        func(*args)
        sides = [i for i in args]
        def Right_sides(s_list):
            s_list = sorted(s_list)
            if s_list[0] + s_list[1] > s_list[-1]:
                perim = sum(s_list)
                p = perim / 2
                print(f'Треугольник возможен\n'
                      f'Его периметр = {perim}\n'
                      f'Его площадь = {sqrt(p * (p - s_list[0]) * (p - s_list[1]) * (p - s_list[2]))}')
            else:
                print('Треугольник не получится')

        if not all(isinstance(i, (int, float)) for i in sides):
            try:
                for i, el in enumerate(sides):
                    sides[i] = float(el)
                Right_sides(sides)
            except ValueError:
                print('Нужно указывать числа')
        else:
            Right_sides(sides)
    return Wrapper


@Triangle
def Set_triangle(side_a, side_b, side_c):
    return side_a, side_b, side_c

Set_triangle('9', 2, 8)

