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

obj1 = Person('Алла', 'Давиденко', 40)
obj2 = Person('Олег', 'Давиденко', 41)
obj3 = Person('Антон', 'Давиденко', 12)
obj4 = Person('Тамара', 'Давиденко', 63)
print(obj1, obj2, obj3, obj4)

class Family(Person):
    """
    Класс описывающий семью
    """
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
    def grandma(self):
        return self.__grandma
    def __init__(self, mother: str, father: str, kid: str, grandmother: str, address: str):
        self.__address = address
        self.__mom = mother
        self.__dad = father
        self.__child = kid
        self.__grandma = grandmother
        super().__init__(self.firstname, self.lastname, self.age)
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address
    def create_dict_(self, data_dict):
        result = []
        for key, value in data_dict.items():
            result.append({'key': key, 'value': value})
        return result

obj = Family('Алла Давиденко, 40, ул. Матросова 90',
             'Олег Давиденко, 41, ул. Матросова 90',
             'Антон Давиденко, 12, ул. Матросова 90',
             'Тамара Давиденко, 63, ул. Матросова 90', 'ул. Матросова 90')
print(obj.mom)
print(obj.dad)
print(obj.child)
print(obj.grandma)
obj.create_dict_({'mom': 'Алла Давиденко, 40, ул. Матросова 90', 'dad': 'Олег Давиденко, 41, ул. Матросова 90',
                  'child': 'Антон Давиденко, 12, ул. Матросова 90', 'grandma': 'Тамара Давиденко, 63, ул. Матросова 90'})
print(obj.create_dict_({'mom': 'Алла Давиденко, 40, ул. Матросова 90', 'dad': 'Олег Давиденко, 41, ул. Матросова 90',
                  'child': 'Антон Давиденко, 12, ул. Матросова 90', 'grandma': 'Тамара Давиденко, 63, ул. Матросова 90'}))




















