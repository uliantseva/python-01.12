class Animals:
    """
     Класс описывающий животных
    """
    def __init__(self, name: str, weight: int, mov_speed: int):
        self.__name = name
        self.__weight = weight
        self.__mov_speed = mov_speed
    @property
    def name(self):
        return self.__name
    @property
    def weight(self):
        return self.__weight
    @property
    def mov_speed(self):
        return self.__mov_speed
    def make_a_sound(self):
        print("Издаёт животный звук")
    def __str__(self):
        return f'название: {self.__name}\nвес: {self.__weight}\nскорость передвижения: {self.__mov_speed}\n'
obj = Animals('hummingbird', 5, 98)
print(obj)


class Birds(Animals):
    """
    Подкласс описывающий птиц
    """
    def __init__(self,  body_length: int, name: str, weight: int, mov_speed: int):
        self.__body_length = body_length
        super().__init__(name, weight, mov_speed)
    @property
    def number_of_feathers(self):
        return self.__body_length
    def make_a_sound(self):
        print("Издаёт животный звук")
    def __str__(self):
        return super().__str__() + f'длина тела: {self.__body_length}\n'
birds = Birds(10,'hummingbird', 5, 10)
print(birds)


class Reptiles(Animals):
    """
    Подкласс описывающий гадов
    """
    def __init__(self, number_of_paws: int, name: str, weight: int, mov_speed: int):
        self.__number_of_paws = number_of_paws
        super().__init__(name, weight, mov_speed)
    @property
    def number_of_paws(self):
        return self.__number_of_paws
    def __str__(self):
        return super().__str__() + f'количество лап: {self.__number_of_paws}\n'
reptiles = Reptiles(4, 'anura', 700, 4)
print(reptiles)


class Mammals(Animals):
    """
    Подкласс описывающий млекопитающих
    """
    def __init__(self, body_length: int, name: str, weight: int, mov_speed: int):
        self.__body_length = body_length
        super().__init__(name, weight, mov_speed)
    @property
    def body_length(self):
        return self.__body_length
    def __str__(self):
        return super().__str__() + f'длинна тела: {self.__body_length}\n'
mammals = Mammals(3,'kangu', 47, 70)
print(mammals)


class Stork(Birds):
    """
    Подкласс описывающий бескилевых птиц
    """
    def __init__(self, type: str, body_length: int, name: str, weight: int, mov_speed: int):
        self.__type = type
        super().__init__(body_length, name, weight, mov_speed)
    @property
    def inf_rank(self):
        return self.__type
    def make_a_sound(self):
        print('АРРР')
    def __str__(self):
        return super().__str__() + f'тип: {self.__type}\n'
stork = Stork('Horde', 110, 'stork', 3, 45)
print(stork)
stork.make_a_sound()

class Ara(Birds):
    """
    Подкласс описывающий новонёбных птиц
    """
    def __init__(self, type: str, families: str,  body_length: int, name: str, weight: int, mov_speed: int):
        self.__type = type
        self.__families = families
        super().__init__(body_length, name, weight, mov_speed)
    @property
    def inf_rank(self):
        return self.__type
    @property
    def families(self):
        return self.__families
    def __str__(self):
        return super().__str__() + f'тип: {self.__type}\nсемейства: {self.__families}\n'
parrot = Ara('Horde', 'Parrot', 80,'ara', 900,100)
print(parrot)



class Amphibia(Reptiles):
    """
    Подкласс описывающий голых гадов
    """
    def __init__(self, body_length: int, number_of_paws: int, name: str, weight: int, mov_speed: int):
        self.__body_length = body_length
        super().__init__(number_of_paws, name, weight, mov_speed)
    @property
    def body_length(self):
        return self.__body_length
    def __str__(self):
        return super().__str__() + f'длинна тела: {self.__body_length}\n'
amphibia = Amphibia(20, 4, 'anura', 700, 4)
print(amphibia)

class Reptilia(Reptiles):
    """
    Подкласс описывающий чешуйчатых гадов
    """
    def __init__(self, detachment: str, number_of_paws: int, name: str, weight: int, mov_speed: int):
        self.__detachment = detachment
        super().__init__(number_of_paws, name, weight, mov_speed)
    @property
    def detachment(self):
        return self.__detachment
    def __str__(self):
        return super().__str__() + f'отряд: {self.__detachment}\n'

reptilia =  Reptilia('crocodilia', 4, 'crocodylus niloticus', 750, 35)
print(reptilia)


class Marsupialia(Mammals):
    """
    Подкласс описывающий сумчатых
    """
    def __init__(self, kinds: str, body_length: int, name: str, weight: int, mov_speed: int):
        self.__kinds = kinds
        super().__init__(body_length, name, weight, mov_speed)
    @property
    def kinds(self):
        return self.__kinds
    def __str__(self):
        return super().__str__() + f'виды: {self.__kinds}\n'
mar = Marsupialia('entomophagy,phytophagy', 3,'kangu', 47, 70)
print(mar)


class Placentalia(Mammals):
    """
    Подкласс описывающий плацентарны
    """
    def __init__(self, superorders: str, body_length: int, name: str, weight: int, mov_speed: int):
        self.__superorders = superorders
        super().__init__(body_length, name, weight, mov_speed)
    @property
    def superorders(self):
        return self.__superorders
    def __str__(self):
        return super().__str__() + f'виды: {self.__superorders}\n'
plac = Placentalia('afrotheria', 7, 'sirenia', 60, 30)
print(plac)