class Employee:
    """Создаем класс Employee"""

    def __init__(self, firstname: str, lastname: str,  age: int, email: str, skills: list,
                 people_lang: list, coding_lang: list):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.skills = skills
        self.people_lang = people_lang
        self.coding_lang = coding_lang

    def save_data_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(f"Name: {self.firstname} {self.lastname}\n")
            file.write(f"Age: {self.age}\n")
            file.write(f"Email: {self.email}\n")
            file.write(f"Skills: {', '.join(self.skills)}\n")
            file.write(f"Languages: {', '.join(self.people_lang)}, {', '.join(self.coding_lang)}\n")

obj = Employee('Ivasik', 'Telesik', 13, 'ivasik-telesik1732@izkurnanog.ua',
               ["ходить", "говорить", "кодить"],
               ["Україньська", "Англійська"],
               ["Python", "C++", "lisp"])
print(obj.firstname, obj.lastname)
print(obj.age)
print(obj.email)
print(obj.skills)
print(obj.people_lang)
print(obj.coding_lang)
obj.save_data_to_file("files/Employee.json")
obj.save_data_to_file("files/Employee.csv")
