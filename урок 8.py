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

## 2
my_list = [1, 2, 3, 4]
my_list.append(my_list.pop())
print(my_list)


## 3
my_str = '43 больше чем 34, но меньше чем 56'
# python style
s = result = sum([int(word) for word in my_str.split() if word.isdigit()])
print(result)

result_str = ' '
for symbol in my_str:
    if symbol.isdigit():
        result_str += symbol
    else:
        result_str += ' '
print(sum(int(number) for number in result))
