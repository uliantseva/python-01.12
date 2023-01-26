"""
ООР
"""
# класс - пользовательский тип данных
class Lamp: # обязателллльно начинается с большой буквы классы
    """

    """
    on = bool()
    power = int()
    temperature = int()
    lamp_socket = str()

    def __init__(self, on, bool, power, int, temperature: int, lamp_socket: str):
        self.on = on
        self.power = power
        self.lamp_socket = lamp_socket
        self.temperature = temperature
        # конструктор объекта
        print('Lamp constructor!!')

# функция в классе называется: методы
# self - указательно содержащий адрес объекта являющегося инициатором вызова данного метода
    def show_parameters(self):
        # обращение к свойствам объекта происходит через указатель self
        print(f''
              f'On: {self.on}\n'
              f'Power:{self.power}\n'
              f'Temperature:{self.temperature}\n'
              f'Socket:{self.lamp_socket}\n'
              f'')
obj = Lamp(100, 5600, 'e27')
obj.show_parameters()
print(obj)
# obj = Lamp()

# obj.power = 100
# obj.show_parameters()

# obj2 = Lamp()
# obj2.show_parameters()
# добавление динамическое свойство объекта
# obj.my_new_data = 'Tigidim'
# print(obj.my_new_data)
# print(obj.my_new_data) # динамическое свойство не передается в другие объекты и не по падает в класс
# print(obj.__dir__())
# print(obj.__doc__)
# print(obj.__dict__) # cловарь определенных свойств объекта
# print(Lamp.__dict__) # cловарь определенных свойств класса