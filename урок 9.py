
from random import randint
cube_dict = {
    1:'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six'
}
value = randint(1, 100)
print(value)
result = cube_dict[value % 6 + 1]
print(f'результат броска кубика {result}')
a = 9
di = {'key': a}
print(di)
a = 3
print(di)
di['key'] = 3
print(di)
