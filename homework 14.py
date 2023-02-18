class Transport:
    """
    Класс описывающий транспорт
    """
    def __init__(self, gov_number: str, number_of_wheels: str, power: str, max_speed: str):
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
        return f'gov_number: {self.__gov_number}\nnumber_of_wheels:{self.__number_of_wheels}\n' \
               f'power: {self.__power}\nmax_speed: {self.__max_speed}\n'
obj = Transport('1Q2EA', '4', '5500', '150')
print(obj)
obj.power('')
