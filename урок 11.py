 #пример функции для обработки файлов
def read_txt_files(filename: str):
    with open(filename, 'rt') as file:        ### более интересна в использованием посравнению со вторым вариантом
         data = file.read()
         return data
    return 0
def write_txt_file(filename: str, data):
    with open(filename, 'wt') as file:
        file.write(str(data))
