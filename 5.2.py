'''

'''
# строка - неизменяемый тип данных,представляет собой последовательность символов является итерируемым объектом

my_string = 'string'
my_string2 = str('another string')
my_string3 = '''multiline
string'''
print(len(my_string)) # len() - функция вохвращающая длинну итерируемого объекта
print(my_string[0]) # обращение к символу по индексу (все начинается с нуля)   сколько элементов надо пропусти
  # чтобы попасть к определенному элементу
print(my_string[-1]) # отрицательные индексы обращаются с конца

'''срезы'''
#string[старт:стоп:шаг] по умолчанию default[0:len(start):1]
print('string[старт:стоп:шаг] default[0:len(start):1]')
print('my_string[0:len(my_string):1]', my_string[0:len(my_string):1])
print('my_string[2:]', my_string[2:])
print('my_string[:4]', my_string[:4])
print('my_string[1:4]', my_string[1:4])
print('my_string[4:1:-1]', my_string[4:1:-1])
print('my_string[::-1]', my_string[::-1])

number = 123456 # преобразование переворот
result = int(str(number) [::-1])
print(result)
