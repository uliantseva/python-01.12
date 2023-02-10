import os
#1
class Directory:
    """
    Инициализация класса с одним параметром
    """
    def __init__(self, directory_name):
        self. directory_name = directory_name
#2
    def create_dic(self):
        """
        метод класса, который создает атрибут класса в ввиде словаря
        :return:
        """
        dirs, files = list(), list()
        for item in os.listdir(self.directory_name):
            if os.path.isdir(os.path.join(self.directory_name, item)):
                dirs.append(item)
            else:
                files.append(item)
        self.listing = {'filenames': files, 'dirnames': dirs}
        return self.listing
#3
    def sort_dict(self, alphabetical=False):
        alphabet_dict = self.create_dic()
        alphabet_dict['filenames'] = sorted(alphabet_dict['filenames'], reverse=alphabetical)
        alphabet_dict['dirnames'] = sorted(alphabet_dict['dirnames'], reverse=alphabetical)
        return alphabet_dict
#4
    def get_string(self, string):
        if '.' in string:
            self.directory_name['filenames'].append(string)
        else:
            self.directory_name['dirnames'].append(string)
        return self.directory_name


obj = Directory(r'C:\Users\Lexx1488\PycharmProjects\pythonProject_28\python-01.12/files')
print(obj.create_dic())
print(obj.sort_dict())
print(obj.get_string('files'))





