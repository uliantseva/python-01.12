try:
    list_of_integers = [0, 1, 2, 3, 4, 5]
    user_index = 15
    print(list_of_integers[user_index])
except IndexError:
    print('Такого индекса не существует')
