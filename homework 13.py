class Person:
    """
    Класс описывающий человека
    """
    __firstname = str()
    __lastname = str()
    __age = int()
    __email = str()
    __phone = str()

    @property
    def firstname(self):
        return self.__firstname
    @property
    def lastname(self):
        return self.__lastname
    @property
    def age(self):
        return self.__age
    @property
    def email(self):
        return self.__email
    @property
    def phone(self):
        return self.__phone
    @email.setter
    def email(self, email: str):
        self.__email = email
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    def __set_age(self, age: int):
        if age >= 0:
            self.__age = age
        else:
            self.__age = 0
    def __init__(self, name: str, surname: str, age: int):
        self.__firstname = name
        self.__lastname = surname
        self.__set_age(age)
    def __str__(self):
        info = f'Name:{self.firstname} Surname:{self.lastname} Age:{self.age}'
        if self.email != '':
            info = f'{info}e-mail:{self.__email}\n'
        if self.phone != '':
            info = f'{info}phone:{self.__email}\n'
        return info
obj = Person('Давиденко', 'Ала', 4)
print(obj)
obj = Person('Давиденко', 'Олег', 46)
print(obj)
obj = Person('Давиденко', 'Антон', 12)
print(obj)
obj = Person('Давиденко', 'Тамара', )
print(obj)


class Family(Person):
    """
    Класс описывающий семью
    """
    __mom = str()
    __dad = str()
    __child = str()
    __grandmother = str()
    @property
    def mom(self):
        return self.__mom
    @property
    def dad(self):
        return self.__dad
    @property
    def child(self):
        return self.__child
    @property
    def grandmother(self):
        return self.__grandmother








