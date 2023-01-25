import homework_module
print('\n', homework_module.my_list)
import homework_module as h_w_mod
h_w_mod.string_list()

# 1
new_list = []
for index in range(len(h_w_mod.my_list)):
    if index % 2:
        new_list.append(h_w_mod.my_list[index][::-1])
    else:
        new_list.append(h_w_mod.my_list[index])
print('\n', 'new_list', new_list)

# 2
my_letters = [letter for letter in h_w_mod.my_list if letter.lower().startswith('a')]
print('\n', 'my_letters', my_letters)

# 3
new_letters = [new_letter for new_letter in h_w_mod.my_list if 'a' in new_letter]
print('\n', 'new_letters', new_letters)



from homework_module import my_list_2
print('\n', my_list_2)

# 4
result = []
for li_str in my_list_2:
    if type(li_str) == str:
        result.append(li_str)
print('result', result)

# 5
from homework_module import my_str
print('\n', my_str)

my_set = set(my_str)
lst = []
for i in my_set:
    if my_str.count(i) == 1:
        lst.append(i)
print('lst', lst)

# 6
from homework_module import str_1, str_2
print('\n', str_1)
print('\n', str_2)

result = [element for element in str_1 if element in str_2]
print('result', result)

# 7
from homework_module import str_3, str_4
print('\n', str_3)
print('\n', str_4)

for i in str_3:
    k = str_3.find(i) - str_3.rfind(i)
    if k == 0:
        if i in str_4 and str_4.find(i) - str_4.rfind(i) == 0:
            print(i)
