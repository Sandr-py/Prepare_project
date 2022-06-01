"""Создание менеджера контекста:
    Реализую работу со списком с использованием менеджера контекста.
"""


class summary:
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

with summary(v1) as list1:
    try:
        for i in range(len(v1)):
            list1[i] += v2[i]
    except Exception as e:
        print(e)

print('Изменённый список v2 ', v1)

with summary(v2) as list_m:
    try:
        new_list = list(filter(lambda x: x % 2 == 0, list_m))
    except Exception as e:
        print(e)

print(v2)
print('Метод работы lambda с v2', new_list)
