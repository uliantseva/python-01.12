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
    def __str__(self):
        return f'название: {self.__name}\nвес: {self.__weight}\nскорость передвижения: {self.__mov_speed}\n'
obj = Animals('hummingbird', 5, 98)
print(obj)

class Birds(Animals):
    """
    Подкласс описывающий птиц
    """
    def __init__(self, number_of_feathers: int, name: str, weight: int, mov_speed: int):
        self.__number_of_feathers = number_of_feathers
        super().__init__(name, weight, mov_speed)
    @property
    def number_of_feathers(self):
        return self.__number_of_feathers
    def __str__(self):
        return super().__str__() + f'количество перьев: {self.__number_of_feathers}\n'
birds = Birds(5000,'hummingbird', 5, 98)
print(birds)

class Paleognathae(Birds):
    """
    Подкласс описывающий бескилевых птиц
    """
    def __init__(self, inf_rank: str, number_of_feathers: int, name: str, weight: int, mov_speed: int):
        self.__inf_rank = inf_rank
        super().__init__(number_of_feathers, name, weight, mov_speed)
    @property
    def inf_rank(self):
        return self.__inf_rank

    def __str__(self):
        return super().__str__() + f'ранг инфракласса: {self.__inf_rank}\n'
pal= Paleognathae('casuariiformes', 5000, 'emu', 37, 50)
print(pal)

class Neognathae(Birds):
    """
    Подкласс описывающий новонёбных птиц
    """
    def __init__(self, families: str, inf_rank: str, number_of_feathers: int, name: str, weight: int, mov_speed: int):
        self.__inf_rank = inf_rank
        self.__families = families
        super().__init__(number_of_feathers, name, weight, mov_speed)
    @property
    def inf_rank(self):
        return self.__inf_rank
    @property
    def families(self):
        return self.__families

    def __str__(self):
        return super().__str__() + f'ранг инфракласса: {self.__inf_rank}\nсемейства: {self.__families}\n'
neo = Neognathae('phasianidae', 'galliformes', 6000,'peacock', 6, 50)
print(neo)

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