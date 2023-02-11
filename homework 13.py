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
        info = f'Name: {self.firstname} Surname: {self.lastname} Age: {self.age}\n'
        if self.email != '':
            info = f'{info}e-mail: {self.__email}\n'
        if self.phone != '':
            info = f'{info}phone: {self.__phone}\n'
        return info

class Family(Person):
    """
    Класс описывающий семью
    """
    __mom = str()
    __dad = str()
    __child = str()
    __grandmother = str()
    __address = str()
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
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address
    def __set_age(self, age: int):
        if age >= 0:
            self.__age = age
        else:
            self.__age = 0
    def __init__(self, person: Person, address):
        super().__init__(person.firstname, person.lastname, person.age)
        self.__address = address
    def __str__(self):
        info = f'Name: {self.firstname} Surname: {self.lastname} Age: {self.age} address: {self.address}'
        if self.email != '':
            info = f'{info}e-mail: {self.__email}\n'
        if self.phone != '':
            info = f'{info}phone: {self.__phone}\n'
        return info
    def get_dict(self):
        data_dict = {}
        data_dict['mom'] = self.firstname, self.lastname, self.age, self.address
        data_dict['dad'] = self.firstname, self.lastname, self.age, self.address
        data_dict['child'] = self.firstname, self.lastname, self.age, self.address
        data_dict['grandmother'] = self.firstname, self.lastname, self.age, self.address
        #for key, value in data_dict.items():
                #([key, value])
        print(data_dict)
        return data_dict

obj1 = Person('Ала', 'Давиденко', 40)
obj1.phone = '0997524589'
obj1.email = 'fghjkk@gmail.com'
print(obj1)
obj2 = Person('Олег', 'Давиденко', 41)
obj2.email = 'dffgy@gmail.com'
obj2.phone = '0507891258'
print(obj2)
obj3 = Person('Антон', 'Давиденко', 12)
print(obj3)
obj4 = Person('Тамара', 'Давиденко', 63)
obj4.phone = '0912365874'
print(obj4)
family = Family(obj1, 'ул. Плехановская 90')
print(family)








