import os
#path = r'C:\Users\Lexx1488\PycharmProjects\pythonProject_28\python-01.12/files'
#data = os.listdir(path)
#print(r'C:\Users\Lexx1488\PycharmProjects\pythonProject_28\python-01.12/files', os.listdir())
#path = r'C:\Users\Lexx1488\PycharmProjects\pythonProject_28\python-01.12/files'

#print(os.path.join('папка', 'файл'))
#os.mkdir(r'files\папка')
#os.makedirs(r'files\files', exist_ok=True)
#with open(r'files\test', 'w'):
    #pass
#print(os.listdir('files'))
#print(os.path.isdir(r'files\test.csv'))
#path = 'files/directory'
#print("Текущая рабочая директория %s" % path)
#1
class Directory:
    """
    Инициализация класса с одним параметром
    """
    def __init__(self, directory_name):
        self. directory_name = directory_name
#2
    def get_dic(self):
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
    def get_new_dic(self, dict):
        dir_list = dict['dirs']
        file_list = dict['files']
        if self.directory_name:
            dir_list.sort()
            file_list.sort()
        else:
            dir_list.sort(reverse=True)
            file_list.sort(reverse=True)
        dict['dir'] = dir_list
        dict['files'] = file_list
        print(dict)
        return dict

obj = Directory(r'C:\Users\Lexx1488\PycharmProjects\pythonProject_28\python-01.12/files')
print(obj.get_dic())
obj.get_new_dic(dict)



