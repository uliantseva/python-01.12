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

#

my_string ='some new string'
print('new_string ->, my_string ')

print('my_string.split() ->', my_string.split())
print('my_string.split(sep="s"->) ->', my_string.split(sep="s"))
print('my_string.upper() ->', my_string.upper())
print('my_string ->', my_string)


symbol = 'a'
print('symbol.isdigit() ->', symbol.isdigit())
print('symbol.isalpha() ->', symbol.isalpha())
print('symbol.isalnum() ->', symbol.isalnum())
text = 'London is the capital of Great Britain'
print(text)
print('text.find("a")', text.find("a"))
print('text.find("ap")', text.find("ap"))
print('text.find("al")', text.find("al"))


print("text.replace('London', 'Kiev')", text.replace('London', 'Kiev'))
print(text)
print("text.replace('Great Britain', '***')", text.replace('Great Britain', '***'))


#родитель f - строк
print('{}, {}, {}')
print('{}, {}, {}'.format(12, 'Strone', 'table'))
print('{1}, {2}, {0}'.format(12, 'Strone', 'table'))
print('{c}, {a}, {b}'.format(a = 12, b = 'Strone', c = 'table'))
