import random
li = [random.randint(1, 1000) for i in range(15)]
for i in li:
    if i > 100:
        print(i, end=':')

###
li = [random.randint(1, 1000) for i in range(15)]
my_result = 0
for i in range(100):
    if my_result > 100:
        print(i, end=' ')
    else:
        print(' ', end=' ')

