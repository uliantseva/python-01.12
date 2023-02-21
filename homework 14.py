class Transport:
    """
    Класс описывающий транспорт
    """
    def __init__(self, gov_number: str, number_of_wheels: int, power: int, max_speed: int):
        self.__gov_number = gov_number
        self.__number_of_wheels = number_of_wheels
        self.__power = power
        self.__max_speed = max_speed
    @property
    def gov_number(self):
        return self.__gov_number
    @property
    def number_of_wheels(self):
        return self.__number_of_wheels
    @property
    def power(self):
        return self.__power
    @property
    def max_speed(self):
        return self.__max_speed

    def __str__(self):
        return f'государственный номер: {self.__gov_number}\nколичество колес: {self.__number_of_wheels}\n' \
               f'мощность двигателя: {self.__power}\nмаксимальная скорость: {self.__max_speed}\n'

obj = Transport('1Q2EA', 4, 1000, 150)
print(obj)

class Bike(Transport):
    """
    Описание подкласса
    """
    def __init__(self, brakes: str, gov_number: str, number_of_wheels: int, power: int, max_speed: int):
        self.__brakes = brakes
        super().__init__(gov_number, number_of_wheels, power, max_speed)
    @property
    def brakes(self):
        return self.__brakes
    def __str__(self):
        return super().__str__() + f'тормоза: {self.__brakes}\n'

bike = Bike('Drum, Rim, Disc', 'номер отсутсвует', 2, 400, 200)
print(bike)
class Car(Transport):
    """
    Описание подкласса
    """
    def __init__(self, engine_number: str, gov_number: str, number_of_wheels: int, power: int, max_speed: int):
        self.__engine_number = engine_number
        super().__init__(gov_number, number_of_wheels, power, max_speed)
    @property
    def engine_number(self):
        return self.__engine_number
    def __str__(self):
        return super().__str__() + f'номер двигателя: {self.__engine_number}\n'

car = Car('2K34HJU', '1Q2EA', 4, 1000, 150)
print(car)

class Bus(Transport):
    """
    Описание подкласса
    """
    def __init__(self, number_of_seats: int, gov_number: str, number_of_wheels: int, power: int, max_speed: int):
        self.__number_of_seats = number_of_seats
        super().__init__(gov_number, number_of_wheels, power, max_speed)
    @property
    def number_of_seats(self):
        return self.__number_of_seats
    def __str__(self):
        return super().__str__() + f'количество мест: {self.__number_of_seats}\n'


bus = Bus(55, 'номер отсутсвует', 4, 1000, 150)
print(bus)
class Motorbike(Bike):
    """
    Описание подкласса
    """
    def __init__(self, moto_mirrors: int, brakes: str, gov_number: str, number_of_wheels: int, power: int, max_speed: int):
        self.__moto_mirrors = moto_mirrors
        super().__init__(brakes, gov_number, number_of_wheels, power, max_speed)
    @property
    def moto_mirrors(self):
        return self.__moto_mirrors
    def __str__(self):
        return super().__str__() + f'зеркала на мотоцикле: {self.__moto_mirrors}\n'
moto = Motorbike(2, 'Drum, Disc', 'AAA56G', 2, 1000, 150)
print(moto)
class Truck(Car):
    """
     Описание подкласса
    """
    def __init__(self, type: str, engine_number: str, gov_number: str, number_of_wheels: int, power: int, max_speed: int):
        self.__type = type
        super().__init__(engine_number, gov_number, number_of_wheels, power, max_speed)
    @property
    def type(self):
        return self.__type
    def __str__(self):
        return super().__str__() + f'тип грузовика: {self.__type}\n'
truck = Truck('закрытый, тентованный', '2K34HJU', '1Q2EA', 4, 1000, 150)
print(truck)