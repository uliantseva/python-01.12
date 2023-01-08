'''

'''
# списки - типы данных позволяющие хранить под одним именем множество разнообразных объектов
 # является итерируемым объектом

my_list = list()
my_list2 = []
my_list3 = [1, 2, 3, 'Vasa', 3.2, my_list]
my_list4 = 'Vasa'
s = 'Vasa asdf asdf asdf sdfvc sdef'
my_list5 = s.split()  ## разделитель
print('my_list ->', my_list)
print('my_list2 ->', my_list2)
print('my_list3 ->', my_list3)
print('my_list4 ->', my_list4)
print('my_list5 ->', my_list5)

#обращение с элементами
#     0  1  2  3  4   5 0   1    2        6
li = [1, 2, 3, 4, 5, ['a', 'b', 'c', ], 'Anatoliy']
print(li[2])
print(li[5])
print(li[5][1]) # обращение к элементу списка в списке

# пример списка в списке - матрица
matrix = [
    [1, 2, 3, 4, 5],
    [2, 4, 1, 5, 6],
    [1, 1, 0, 3, 5],
]
print('li[2:5]', li[2:5]) # срез
print('li[-2]', li[-2])  # отрицательный индекс

#перебор списка по индексу
print('''for index in range(len(li)):
         print(index, end=' ' ''')
########




#

