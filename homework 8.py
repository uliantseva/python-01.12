import homework8_example_module
homework8_example_module.fun()
print('homework8_example_module.my_list', homework8_example_module.my_list)


# 1
def function():
    str1 = 'ad'
    str2 = 'as'
    str3 = 'gh'
    return[str1, str2, str3]
li = function()
print('li', li)
new_li = []
for index in range(len(li)):
    if index % 2:
        new_li.append(li[index][::-1])
    else:
        new_li.append(li[index])
print('new_li', new_li)


# 3
new_list = [new_list for new_list in li if "a" in new_list]
print(new_list)






