import homework8_example_module
homework8_example_module.fun()
print('homework8_example_module.my_list', homework8_example_module.my_list)


# 1
def function():
    str1 = 'adfg'
    str2 = 'ashj'
    str3 = '325'
    str4 = 'bhai'
    return[str1, str2, str3, str4]
li = function()
print('li', li)
new_list = []
for index in range(len(li)):
    if index % 2:
        new_list.append(li[index][::-1])
    else:
        new_list.append(li[index])
print('new_list', new_list)
# 2
my_letters = [letter for letter in li if letter.lower().startswith('a')]
print('my_letters', my_letters)
# 3
new_letters = [new_letter for new_letter in li if 'a' in new_letter]
print('new_letters', new_letters)

# 4
def fun_1():
    str1 = 'adfg'
    str2 = 'ashj'
    str3 = 325
    str4 = 4789
    return[str1, str2, str3, str4]
li_2 = fun_1()
print('li_2', li_2)
result = []
for li_str in li_2:
    if type(li_str) == str:
        result.append(li_str)
print('result', result)

# 5
def fun_names(my_str):
    """
    asdfdf
    :param my_str:
    :return:
    """
    print(my_str)
    my_set = set(my_str)
    lst = []
    for i in my_set:
        if my_str.count(i) == 1:
            lst.append(i)
    print(lst)
fun_names(my_str='asdfdf')

# 6
def names(str_1, str_2='cap'):
    """
    str_1 = 'asdgjkl'
    str_2 = 'asdfdfg'
    :param str_1:
    :param str_2:
    :return:
    """
    print(str_1, str_2)
    result = []
    for i in str_1:
        k = str_1.find(i) + str_1.rfind(i)
        if k == 0:
            if i in str_2 and str_2.find(i) + str_2.rfind(i) == 0:
                print(i)
                result.append(i)
names(str_1 = 'asdgjkl', str_2 = 'asdfdfg')
# 7
def names(str_3, str_4='cap'):
    """
    str_3 = 'asdfasg'
    str_4 = 'asdfdfg'
    :param str_3:
    :param str_4:
    :return:
    """
    print(str_3, str_4)
    result = []
    for i in str_3:
        k = str_3.find(i) - str_3.rfind(i)
        if k == 0:
            if i in str_4 and str_4.find(i) - str_4.rfind(i) == 0:
                print(i)
                result.append(i)
names(str_3 = 'asdfasg', str_4 = 'asdfdfg')






