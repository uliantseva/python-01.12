import json
import csv
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

    def save_data_to_file(self):
        data_dict = {}
        data_dict['firstname'] = self.firstname
        data_dict['lastname'] = self.lastname
        data_dict['age'] = self.age
        data_dict['email'] = self.email
        data_dict['skills'] = self.skills
        data_dict['people_lang'] = self.people_lang
        data_dict['coding_lang'] = self.coding_lang
        with open("files/Employee.json", 'w') as file:
            json.dump(data_dict, file, indent=4)
        with open("files/Employee.csv", 'w') as file:
            csv_writer = csv.writer(file)
            for key, value in data_dict.items():
                csv_writer.writerow([key, value])
        print(data_dict)
        return data_dict


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
obj.save_data_to_file()

