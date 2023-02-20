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
    def __init__(self, brakes: str, gov_number, number_of_wheels, power, max_speed):
        self.__brakes = brakes
        super().__init__(gov_number, number_of_wheels, power, max_speed)
    @property
    def brakes(self):
        return self.__brakes
    def __str__(self):
        f'государственный номер: {self.__gov_number}\nколичество колес: {self.__number_of_wheels}\n' \
        f'мощность двигателя: {self.__power}\nмаксимальная скорость: {self.__max_speed}\n' \
        f'тормоза: {self.__brakes}\n'
bik = Bike('Drum, Rim, Disc', 'номер отсутсвует', 2, 400, 200)
print(bik.brakes)
print(bik.gov_number)
class Car(Transport):
    pass
class Bus(Transport):
    pass

