class Transport:
    """
    Класс описывающий транспорт
    """
    __state_num = str()
    __num_wheels = int()
    __power = int()
    __max_speed = int()
    def __init__(self, state_num: str, num_wheels: int, power: int, max_speed: int):
        self.__state_num = state_num
        self.__num_wheels = num_wheels
        self.__power = power
        self.__max_speed = max_speed
    def drive(self):
        return f'Транспортное средство движется'
    @property
    def drive_(self):
        return self.drive()
    @property
    def state_num(self):
        return self.__state_num
    @property
    def num_wheels(self):
        return self.num_wheels
    @property
    def power(self):
        return self.__power
    @property
    def max_speed(self):
        return self.__max_speed
    def __str__(self):
        return f'\nгосударственный номер: {self.__state_num}\nколичество колес: {self.__num_wheels}\n' \
               f'мощность двигателя: {self.__power}\nмаксимальная скорость: {self.__max_speed}\n'

transport_obj = Transport('1Q2EA', 4, 1000, 180)
print(transport_obj)
transport_obj.drive()
print(transport_obj.drive())

class Bike(Transport):
    """
    Подкласс описывающий велосипед
    """
    def __init__(self, state_num: str, num_wheels: int, power: int, max_speed: int, num_of_pedals: int):
        self.__num_of_pedals = num_of_pedals
        super().__init__(state_num, num_wheels, power, max_speed)
    @property
    def num_of_pedals(self):
        return self.__num_of_pedals
    def drive_bike(self):
        return super().drive() + f' на {self.__num_of_pedals} колесах\n'
    def __str__(self):
        return super().__str__() + f'количество педалей: {self.__num_of_pedals}\n'

bike_obj = Bike('RG456S', 2, 400, 200, 2)
print(bike_obj)
bike_obj.drive_bike()
print(bike_obj.drive_bike())

class Car(Transport):
    """
    Подкласс описывающий легковую машину
    """
    def __init__(self, state_num: str, num_wheels: int, power: int, max_speed: int, passengers: int, engine_number: int):
        self.__engine_number = engine_number
        self.__passengers = passengers
        super().__init__(state_num,  num_wheels, power, max_speed)
    @property
    def engine_number(self):
        return self.__engine_number
    @property
    def passengers(self):
        return self.__passengers
    def open_door(self):
        if self.__passengers == 0:
            print('Ты можешь открыть дверь\n')
        else:
            print('Ты не можешь открыть дверь\n')
    def __str__(self):
        return super().__str__() + f'количество пассажиров: {self.__passengers}\nномер двигателя: {self.__engine_number}\n'

car_obj = Car('1Q2EA', 4, 1000, 180, 2, 4567)
print(car_obj)
car_obj.open_door()

class Bus(Transport):
    """
    Подкласс описывающий автобус
    """
    def __init__(self, state_num: str, num_wheels: int, power: int, max_speed: int, num_of_seats: int):
        self.__num_of_seats = num_of_seats
        super().__init__(state_num,  num_wheels, power, max_speed)
    @property
    def num_of_seats(self):
        return self.__num_of_seats
    def move_bus(self):
        print('Автобус везет пассажииров,в котором\t'+f'количество мест {self.__num_of_seats}\n')
    def __str__(self):
        return super().__str__() + f'количество мест для пассажиров: {self.__num_of_seats}\n'

bus_obj = Bus('456GHJ', 4, 1000, 150, 55)
print(bus_obj)
bus_obj.move_bus()
class Motorbike(Bike):
    """
    Подкласс описывающий мотоцикл
    """
    def __init__(self, state_num: str, num_wheels: int, power: int, max_speed: int, num_of_pedals: int, gear_num: int):
        self.__gear_num = gear_num
        super().__init__(state_num, num_wheels, power, max_speed, num_of_pedals)
    @property
    def moto_mirrors(self):
        return self.__gear_num
    def speed_gear(self):
        if self.__gear_num >= 3:
            print('Мотоциклист одевает шлем\n')
        else:
            print('Мотоциклист едет без шлема\n')
    def __str__(self):
        return super().__str__() + f'скорость передачи: {self.__gear_num}\n'

moto_obj = Motorbike('AAA56G', 2, 160, 200, 2, 1)
print(moto_obj)
moto_obj.speed_gear()

class Truck(Car):
    """
     Подкласс описывающи грузовик
    """
    def __init__(self, state_num: str, num_wheels: int, power: int, max_speed: int, engine_number: int,
                 passengers: int, carrying: int):
        self.__carrying = carrying
        super().__init__(state_num, num_wheels, power, max_speed, engine_number, passengers)
    @property
    def type(self):
        return self.__carrying
    def load_cargo(self, cargo):
        if self.__carrying - cargo >= 0:
            print(f'Загрузить {cargo} тонны груза')
            self.__carrying -= cargo
        else:
            print(f'Не может загрузить {cargo} тонн груза, осталось только {self.__carrying} тонн')
    def __str__(self):
        return super().__str__() + f'тонн груза: {self.__carrying}\n'
truck_obj = Truck('2K34HJU', 4, 1000, 150, 200, 0, 500)
print(truck_obj)
truck_obj.load_cargo(1000)

