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
obj1_obj2_obj3_obj4 = Person('name', 'surname', 0)
obj1 = Person('Алла', 'Давиденко', 40)
#obj1.phone = '0997524589'
#obj1.email = 'fghjkk@gmail.com'
#print(obj1)
obj2 = Person('Олег', 'Давиденко', 41)
#obj2.email = 'dffgy@gmail.com'
#obj2.phone = '0507891258'
#print(obj2)
obj3 = Person('Антон', 'Давиденко', 12)
#obj3.phone = '0502367895'
#print(obj3)
obj4 = Person('Тамара', 'Давиденко', 63)
#obj4.phone = '0912365874'
#print(obj4)
print(obj1, obj2, obj3, obj4)



class Family(Person):
    """
    Класс описывающий семью
    """
    __mom = str()
    __dad = str()
    __child = str()
    __grandma = str()
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
    def grandma(self):
        return self.__grandma
    def __init__(self, firstname, lastname, age, address):
        self.__address = address
        super().__init__(firstname, lastname, age)
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address
    def __str__(self):
        return f'Name: {self.firstname} Surname: {self.lastname} Age: {self.age} address:{self.address}\n'
    def create_dict(self):
        self.data_dict = {'mom': {'firstname', 'lastname', 'age', 'address'},
                    'dad': {'firstname', 'lastname', 'age', 'address'},
                    'child': {'firstname', 'lastname', 'age', 'address'},
                    'grandma': {'firstname', 'lastname', 'age', 'address'}}
        return self.data_dict
    def get_dict(self):
        new_data_dict = {}
        new_data_dict['mom'] = self.firstname, self.lastname, self.age, self.address
        new_data_dict['dad'] = self.firstname, self.lastname, self.age, self.address
        new_data_dict['child'] = self.firstname, self.lastname, self.age, self.address
        new_data_dict['grandma'] = self.firstname, self.lastname, self.age, self.address
        #print(new_data_dict)
        return new_data_dict
    #def __dict__(self):
        #return f'mom: {self.firstname, self.lastname, self.age, self.address} dad: {self.firstname, self.lastname, self.age, self.address} child: {self.firstname, self.lastname, self.age, self.address} grandma {self.firstname, self.lastname, self.age, self.address}'

obj =  Family('name', 'surname', 0, 'address')
print(obj1_obj2_obj3_obj4)
obj1 = Family('Алла', 'Давиденко', 40, 'ул. Плехановская 90')
print(obj1)
obj2 = Family('Олег', 'Давиденко', 41, 'Плехановская 90')
print(obj2)
obj3 = Family('Антон', 'Давиденко', 12, 'ул. Плехановская 90')
print(obj3)
obj4 = Family('Тамара', 'Давиденко', 63, 'ул. Плехановская 90')
print(obj4)
#print(obj1, obj2, obj3, obj4)
obj.create_dict()
print(obj.create_dict())
#print(obj1.create_dict(), obj2.create_dict(), obj3.create_dict(), obj4.create_dict())
obj.get_dict()
print(obj1.get_dict(), obj2.get_dict(), obj3.get_dict(), obj4.get_dict())




















