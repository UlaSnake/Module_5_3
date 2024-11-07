class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

# Пример использования класса
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Печать объектов
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Название: ЖК Акация, кол-во этажей: 20

# Сравнение этажей
print(h1 == h2)  # False

# Увеличение этажей на 10
h1 = h1 + 10  # Увеличиваем этажи h1 на 10
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 20
print(h1 == h2)  # True

# Увеличение этажей на 10 с помощью __iadd__
h1 += 10  # Увеличиваем h1 еще на 10
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 30

# Увеличиваем этажи h2 на 10 с помощью __radd__
h2 = 10 + h2  # Увеличиваем h2 на 10
print(h2)  # Название: ЖК Акация, кол-во этажей: 30

# Сравнение с разными операторами
print(h1 > h2)   # False
print(h1 >= h2)  # True
print(h1 < h2)   # False
print(h1 <= h2)  # True
print(h1 != h2)  # False