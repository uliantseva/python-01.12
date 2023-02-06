import os
path = r'files'
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
    def get_attributes_dic(self):
        """
        метод класса, который создает атрибут класса в ввиде словаря
        :return:
        """
        dir_list = os.listdir(self. directory_name)
        files_list = []
        dirs_list = []
        for item in dir_list:
            if os.path.isfile(os.path.join(self. directory_name, item)):
                files_list.append(item)
            elif os.path.isdir(os.path.join(self. directory_name, item)):
                dirs_list.append(item)
                print(dirs_list)
                self.dir_attributes = {'filenames': files_list, 'dirnames': dirs_list}
                print(self.dir_attributes)
                print("filenames:", "dirnames:")

obj=Directory('все файлы')

obj.get_attributes_dic()




