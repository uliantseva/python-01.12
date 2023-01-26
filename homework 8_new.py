import homework_module
print('\n', homework_module.my_list)
print('\n', homework_module.my_list_2)
print('\n', homework_module.my_str)
print('\n', homework_module.str_1, homework_module.str_2)
print('\n', homework_module.str_3, homework_module.str_4)

import homework_module as h_w_mod



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
print('my_letters', my_letters)

# 3
new_letters = [new_letter for new_letter in h_w_mod.my_list if 'a' in new_letter]
print('new_letters', new_letters)

# 4
result = []
for li_str in h_w_mod.my_list_2:
    if type(li_str) == str:
        result.append(li_str)
print('result', result)

# 5
my_set = set(h_w_mod.my_str)
lst = []
for i in my_set:
    if h_w_mod.my_str.count(i) == 1:
        lst.append(i)
print('lst', lst)

# 6
result = [element for element in h_w_mod.str_1 if element in h_w_mod.str_2]
print('result', result)

# 7
for i in h_w_mod.str_3:
    k = h_w_mod.str_3.find(i) - h_w_mod.str_3.rfind(i)
    if k == 0:
        if i in h_w_mod.str_4 and h_w_mod.str_4.find(i) - h_w_mod.str_4.rfind(i) == 0:
            print(i)
