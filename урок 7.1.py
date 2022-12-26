'''
генераторы списков
'''
from random import randint
#    randint(start, end) - функция генерирует случайное число из диапазона start - end
print(randint(-22, 9))

'''
li = [expression for item in interable]
expression - выражение 
item - элемент извлекаемый из последователльности
interable - последовательность
'''
li = [i ** 2 for i in range(10)]
print(li)
li = [randint(-100, 100) for i in range(20)]
print(li)

'''
li = [expression for item in interable if condition]
expression - выражение 
item - элемент извлекаемый из последователльности
interable - последовательность
condition - условная конструкция, добавляние элемента произойдет только если она вернет True
'''

my_string = '11 футболистов за 5 лет забили 231 гол в 102 матчах'
li = [word for word in my_string.split() if word.isdigit()]
print(li)
li = [word for word in my_string.split() if word.isalpha()]
print(li)

li = [word for word in my_string if word.isdigit()]
print(li)
li = [word for word in my_string if word.isalpha()]
print(li)

'''
Кортеж - тип данных, является НЕИЗМЕНЯЕМЫМ списком
'''
tu = tuple([1, 2, 3, 4, 5])
tu2 = ('1', 2, 3.2, 'Taras')
tu3 = tuple('apple')
print(tu)
print(tu2)
print(tu3)

