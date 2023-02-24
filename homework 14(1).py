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
    @property
    def speed(self):
        return self.__speed
    def set_weight(self, weight):
        if weight > 0:
            self.__weight = weight
    def get_weight(self):
        return self.__weight
    def set_speed(self, speed):
        if speed > 0:
            self.__speed = speed
    def get_speed(self):
        return self.__speed
    def make_a_sound(self):
        return f'Издает звуки'
    def __str__(self):
        return f'название: {self.__name}, вес: {self.__weight} кг, скорость передвижения: {self.__speed} км/ч, '
obj = Animals('Волк', 50, 160)
print(obj)
obj.make_a_sound()
print(obj.make_a_sound())

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
        return super().make_a_sound() + f' щебетания'

    def __str__(self):
        return super().__str__() + f'длина тела: {self.__body_length} см, '
birds = Birds('Лебедь', 5, 2200, 110)
print(birds)
birds.make_a_sound()
print(birds.make_a_sound())

class Reptiles(Animals):
    """
    Подкласс описывающий рептилий
    """
    def __init__(self, name: str, weight: int, speed: int, num_of_paws: int):
        self.__num_of_paws = num_of_paws
        super().__init__(name, weight, speed)
    @property
    def num_of_paws(self):
        return self.__num_of_paws
    def set_num_of_paws(self, num_of_paws):
        if num_of_paws <= 0:
            print(f'{self.name} ползает')
        else:
            print(f'{self.name} ходит')
    def __str__(self):
        return super().__str__() + f' количество лап: {self.__num_of_paws}, '
reptiles = Reptiles('Черепаха', 3, 35, 4)
print(reptiles)
reptiles.set_num_of_paws(4)
reptiles_1 = Reptiles('Змея', 1, 40, 0)
print(reptiles_1)
reptiles_1.set_num_of_paws(0)

class Mammals(Animals):
    """
    Подкласс описывающий млекопитающих
    """
    def __init__(self, name: str, weight: int, speed: int, body_length: int, hunter: str):
        self.__body_length = body_length
        self.__hunter = hunter
        super().__init__(name, weight, speed)
    @property
    def body_length(self):
        return self.__body_length
    @property
    def hunter(self):
        return self.__hunter
    def set_hunter(self):
        print(f'{self.name} млекопиющее, которое может охотится: {self.__hunter}')
    def set_body_length(self,body_length):
        if body_length >= 0:
            self.__body_length = body_length
    def get_body_length(self):
        return self.__body_length
    def __str__(self):
        return super().__str__() + f'длинна тела: {self.__body_length} см, охотник: {self.__hunter}, '
mammals = Mammals('Волк', 50, 60, 160, 'Да')
print(mammals)
mammals.set_hunter()

class Stork(Birds):
    """
    Подкласс описывающий класс лебедей, его вес, скорость передвижения, длинну тела
    """
    def __init__(self, name: str, weight: int, speed: int, body_length: int, predator: str):
        self.__predator = predator
        super().__init__(name, weight, speed, body_length)
    @property
    def predator(self):
        return self.__predator
    def predator_(self):
        print(f'{self.name} является хищником? {self.__predator} ')
    def __str__(self):
        return super().__str__()
stork = Stork('Аист', 3, 110, 41, 'Нет')
print(stork)
stork.predator_()

class Ara(Birds):
    """
    Подкласс описывающий класс попугая ару, ее вес, скорость передвижения, длинну тела, цвет, клюв
    """
    def __init__(self, name: str, weight: int, speed: int, body_length: int, color: str, beak: str):
        self.__color = color
        self.__beak = beak
        super().__init__(name, weight, speed, body_length)
    @property
    def color(self):
        return self.__color
    @property
    def beak(self):
        return self.__beak
    def set_color(self, color):
        self.__color = color
    def describe_color(self):
        if self.__color == 'красный, синий, желтый':
            print(True)
        else:
            print(False)
    def set_beak(self, beak):
        self.__beak = beak
    def describe_beak(self):
        if self.__beak == 'загнутый':
            print(True)
        else:
            print(False)
    def __str__(self):
        return super().__str__() + f'цвет: {self.__color}, клюв: {self.__beak} '
ara = Ara('Ара', 1, 900, 97, 'красный, синий, желтый', 'загнутый')
print(ara)
ara.describe_color()
ara.describe_beak()

class Fish(Reptiles):
    """
    Подкласс описывающий класс рыб, ее вес, скорость передвижения
    """
    def __init__(self, name: str, weight: int, speed: int, num_of_paws: int, can_swim: str):
        self.__can_swim = can_swim
        super().__init__(name, weight, speed, num_of_paws)
    def get_can_swim(self):
        return self.__can_swim
    @property
    def can_swim(self):
        return self.__can_swim
    def can_swim_(self):
        print(f'Все рыбы плавают: {self.__can_swim}')
    def __str__(self):
        return super().__str__() + f'может плавать: {self.__can_swim}, '
fish = Fish('Акула', 680, 19, 0, 'Да')
print(fish)
fish.can_swim_()

class Frogs(Reptiles):
    """
    Подкласс описывающий класс лягушек, ее вес, скорость передвижения, количество лап
    """
    def __init__(self, name: str, weight: int, speed: int, num_of_paws: int, can_jump: str):
        self.__can_jump = can_jump
        super().__init__(name, weight, speed, num_of_paws)
    @property
    def can_swim(self):
        return self.__can_jump
    def sett_can_jump(self):
        print(f'{self.name} прыгает на расстояние до 10 м')
    def __str__(self):
        return super().__str__() + f'может прыгать: {self.__can_jump}, '
frogs =  Frogs('Лягушкa', 1, 10 , 4, 'Да')
print(frogs)
frogs.sett_can_jump()

class Giraffe(Mammals):
    """
    Подкласс описывающий класс жирафа, ее вес, скорость передвижения, длинну тела, шею, рост
    """
    def __init__(self, name: str, weight: int, speed: int, body_length: int, hunter: str, neck: int, height: int):
        self.__neck = neck
        self.__height = height
        super().__init__(name, weight, speed, body_length, hunter)
    @property
    def neck(self):
        return self.__neck
    @property
    def height(self):
        return self.__height
    def half_growth(self):
        return self.__neck / (self.__neck*2)
    def __str__(self):
        return super().__str__() + f'динна шеи: {self.__neck} см, рост: {self.__height} м'
giraffe =Giraffe('Жираф', 1000, 60, 420, 'Нет', 240, 5)
print(giraffe)
giraffe.half_growth()
print(giraffe.half_growth())

class Bear(Mammals):
    """
    Подкласс описывающий класс медведяб
    """
    def __init__(self, name: str, weight: int, speed: int, body_length: int, hunter: str, can_eat: str):
        self.__can_eat = can_eat
        super().__init__(name, weight, speed, body_length, hunter)
    @property
    def can_eat(self):
        return self.__can_eat
    def can_eat_(self):
            print('Едят растительную, животную или грибную пищу')
    def _hunter_(self):
        return super().set_hunter()
    def __str__(self):
        return super().__str__() + f'питание: {self.__can_eat} '
bear = Bear('Медведь', 500, 40, 3, 'Нет', 'растительную, животную и грибную пищу')
print(bear)
bear._hunter_()
bear.can_eat_()

