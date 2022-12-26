'''
множество - неупорядоченный набор уникальных элементов
'''
my_set = set([1, 2, 3, 4, 5, 6])
print(my_set)
my_set.add(33)
print(my_set)
my_set = {'q', 'w', 'e', 'r', 't', 'y'}
print(my_set)
my_set.add(33)
print(my_set)
my_string = '11 футболистов за 5 лет забили 231 гол в 102 матчах'
my_set = set(my_string)
print(my_set)

my_set.update('Odarka')
print(my_set)
# удаление
my_set.discard('r')
print(my_set)
my_set.discard('w') # discard - исключает элемент в случае ее отсутствия во множестве нет ошибки
print(my_set)
my_set.remove(33)
print(my_set)
