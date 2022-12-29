## 4
my_str = "My long string"
l_limit = "o"
r_limit = "g"
sub_str = []
l_index = my_str.find(l_limit)
r_index = my_str.rfind(r_limit)
print(my_str[l_index + 1:r_index])




