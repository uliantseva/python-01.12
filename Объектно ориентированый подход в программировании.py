"""
ООР
"""
# класс - пользовательский тип данных
class Lamp:
    on = bool()
    power = int()
    temperature = int()
    lamp_socket = str()
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
obj = Lamp()
obj.power = 100
obj.show_parameters()
obj2 = Lamp()
obj2.show_parameters()
