from random import randint
### 1
my_list = [randint(100, 1000) for i in range(20)]
print('my_list', my_list)

### 2
my_list = [randint(100, 500) for h in range(10)]
my_results = my_list
print('my_results', my_results)


### 3
my_list = [1, 2, 3, 4, 5]
if len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
else:
    my_list.append(0)
print(my_list)
print(sum(my_list[-2:]))











