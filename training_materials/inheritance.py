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