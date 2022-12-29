from random import randint
### 1
my_list = [randint(100, 1000) for i in range(20)]
print('my_list', my_list)

### 2
from random import randint
my_list = [randint(1, 500) for i in range(20)]
my_result = []
for i in my_list:
    if i > 100:
        my_result.append(i)
for i in my_result:
    print(i, end=' ')



### 3
my_list = [1, 2, 3, 4, 5]
if len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
else:
    my_list.append(0)
print(my_list)
print(sum(my_list[-2:]))











