## 4
my_str = "My long string"
l_limit = "o"
r_limit = "g"
sub_str = []
l_index = my_str.find(l_limit)
r_index = my_str.rfind(r_limit)
print(my_str[l_index + 1:r_index])

#си версия
for index in range(len(my_str)):
    if my_str[index] == l_limit:
        l_index = index + 1
    break
for index in range(len(-1, len(my_str)):
       if my_str[index] == r_limit:
       r_index = index
    break
print(my_str[l_index:r_index])


