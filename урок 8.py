# 1
my_list = [1, 2, 3, 4]
new_list = my_list[1:].copy()
new_list.append(my_list[0])

new_list = my_list[1:] + my_list[0:1] #  python style

new_list = my_list[1:] + [my_list[0]]   #  3 вариант

new_list = my_list.copy() ##
new_list.append(new_list.pop(0))

new_list = []
for index in range(1,len(my_list)):
    new_list.append(my_list[index])
new_list.append(my_list[0])

print(new_list)
