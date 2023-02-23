class Animals:
    """
     Класс описывающий животных
    """
    def __init__(self, name: str, weight: int, speed: int):
        self.__name = name
        self.__weight = weight
        self.__speed = speed
    @property
    def name(self):
        return self.__name
    @property
    def weight(self):
        return self.__weight
    def set_weight(self, weight):
        if weight > 0:
            self.__weight = weight
    def get_weight(self):
        return self.__weight
    @property
    def speed(self):
        return self.__speed
    def set_speed(self, speed):
        if speed > 0:
            self.__weight = speed
    def get_speed(self):
        return self.__speed
    def __str__(self):
        return f'название: {self.__name}, вес: {self.__weight} кг, скорость передвижения: {self.__speed} км/ч, '
obj = Animals('Волк', 50, 160)
print(obj)

class Birds(Animals):
    """
    Подкласс описывающий птиц
    """
    def __init__(self, name: str, weight: int, speed: int, body_length: int):
        self.__body_length = body_length
        super().__init__(name, weight, speed)
    @property
    def body_length(self):
        return self.__body_length
    def set_body_length(self, body_length):
        if body_length >= 0:
            self.__body_length = body_length
    def get_body_length(self):
        return self.__body_length
    def make_a_sound(self):
        print('Издаёт щебетание\n')
    def __str__(self):
        return super().__str__() + f'длина тела: {self.__body_length} см, '
birds = Birds('Лебедь', 5, 2200, 110)
print(birds)
birds.make_a_sound()

class Reptiles(Animals):
    """
    Подкласс описывающий гадов
    """
    def __init__(self, name: str, weight: int, speed: int, num_of_paws: int):
        self.__num_of_paws = num_of_paws
        super().__init__(name, weight, speed)
    @property
    def num_of_paws(self):
        return self.__num_of_paws
    def set_num_of_paws(self, num_of_paws):
        if num_of_paws >= 0:
            self.__num_of_paws = num_of_paws
    def get_num_of_paws(self):
        return self.__num_of_paws
    def movement_speed(self):
        print(f'{self.name} издает звук\n')
    def __str__(self):
        return super().__str__() + f' количество лап: {self.__num_of_paws}, '
reptiles = Reptiles('Озёрная лягушка', 1, 4, 4)
print(reptiles)
reptiles.movement_speed()
class Mammals(Animals):
    """
    Подкласс описывающий млекопитающих
    """
    def __init__(self, name: str, weight: int, speed: int, body_length: int):
        self.__body_length = body_length
        super().__init__(name, weight, speed)
    @property
    def body_length(self):
        return self.__body_length
    def set_body_length(self,body_length):
        if body_length >= 0:
            self.__body_length = body_length
    def get_body_length(self):
        return self.__body_length
    def __str__(self):
        return super().__str__() + f'длинна тела: {self.__body_length} см, '
mammals = Mammals('Волк', 50, 60, 150)
print(mammals)

class Stork(Birds):
    def __init__(self, name: str, weight: int, speed: int, body_length: int, predator: str):
        self.__predator = predator
        super().__init__(name, weight, speed, body_length)
    @property
    def predator(self):
        return self.__predator
    def __str__(self):
        return super().__str__() + f'является ли хищником: {self.__predator}, '
stork = Stork('Птица', 3, 110, 41, 'Нет' )
print(stork)
#stork.make_a_sound()

class Ara(Birds):
    def __init__(self, name: str, weight: int, speed: int, body_length: int, color: str):
        self.__color = color
        super().__init__(name, weight, speed, body_length)
    @property
    def color(self):
        return self.__color
    def set_color(self, color):
            self.__color = color
    def __str__(self):
        return super().__str__() + f'цвет: {self.__color}, '
ara = Ara('Попугай', 1, 900, 97, 'красный-синий-желтый')
print(ara)

class Fish(Reptiles):
    def __init__(self, name: str, weight: int, speed: int, num_of_paws: int, can_swim: str):
        self.__can_swim = can_swim
        super().__init__(name, weight, speed, num_of_paws)
    def get_can_swim(self):
        return self.__can_swim
    @property
    def can_swim(self):
        return self.__can_swim
    @can_swim.setter
    def can_swim(self, can_swim):
        self.__can_swim = can_swim
    def __str__(self):
        return super().__str__() + f'может плавать: {self.__can_swim}, '
fish = Fish('Акула', 680, 19, 0, 'Да')
print(fish)

class Frogs(Reptiles):
    """
    Подкласс описывающий чешуйчатых гадов
    """
    def __init__(self, name: str, weight: int, speed: int, num_of_paws: int, can_swim: str):
        self.__can_swim = can_swim
        super().__init__(name, weight, speed, num_of_paws)
    @property
    def can_swim(self):
        return self.__can_swim
    def can_swim_(self):
        print(f'{self.name} прыгают')
    def __str__(self):
        return super().__str__() + f'может плавать: {self.__can_swim}, '

frogs =  Frogs('Лягушки', 1, 750, 4, 'Да')
print(frogs)
frogs.can_swim_()

class Marsupialia(Mammals):
    """
    Подкласс описывающий сумчатых
    """
    def __init__(self, name: str, weight: int, speed: int, body_length: int, kinds: str,):
        self.__kinds = kinds
        super().__init__(name, weight, speed, body_length)
    @property
    def kinds(self):
        return self.__kinds
    def __str__(self):
        return super().__str__() + f'виды: {self.__kinds}\n'
#mar = Marsupialia('entomophagy,phytophagy', 3,'kangu', 47, 70)
#print(mar)


class Placentalia(Mammals):
    """
    Подкласс описывающий плацентарны
    """
    def __init__(self, name: str, weight: int, speed: int, body_length: int, superorders: str):
        self.__superorders = superorders
        super().__init__(name, weight, speed, body_length)
    @property
    def superorders(self):
        return self.__superorders
    def __str__(self):
        return super().__str__() + f'виды: {self.__superorders}\n'
#plac = Placentalia('afrotheria', 7, 'sirenia', 60, 30)
#print(plac)