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

heft = KgToPounds(10)
print(heft.kg)
heft.kg = 5
print(heft.kg)