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