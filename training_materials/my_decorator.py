"""Написание собственного декоратора"""

from math import sqrt


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
                      f'Его площадь = {sqrt(p * (p - s_list[0]) * (p - s_list[1]) * (p - s_list[2]))}\n\n')
            else:
                print('Треугольник не получится\n\n')

        if not all(isinstance(i, (int, float)) for i in sides):
            try:
                for i, el in enumerate(sides):
                    sides[i] = float(el)
                Right_sides(sides)
            except ValueError:
                print('Нужно указывать числа \n\n')
        else:
            Right_sides(sides)
    return Wrapper


@Triangle
def Set_triangle(side_a, side_b, side_c):
    return side_a, side_b, side_c


Set_triangle(2, 2, 2)
Set_triangle(10, 5, 2)
Set_triangle('9', 2, 8)
Set_triangle('Привет', 2, 8)
