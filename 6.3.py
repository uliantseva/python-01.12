# методы списков
li = [1, 2, 3, 4, 5, 6, 7]
print('li', li)
li.append('blabla')    # добавление в конце списка
print('li', li)
li.insert(3, [11, 22, 33])    # добавление в заднюю позицию (индекс)
print('li', li)
del(li[4])  # удаление элемента по идексу
print('li', li)
li.remove(5)   # удаляет по значению
print('li', li)
print(li.pop(5))   #   выдавливает из списка и возвращает его
print('li', li)



li = [3, 2, 6, 8, 1, 9, 5, 2]
print('li.count(2)', li.count(2))
del(li[3])
li.sort()
print('li', li)
li.sort(reverse=True)   # сортировка в обратном порядке от большего к меньшему
print('li', li)


