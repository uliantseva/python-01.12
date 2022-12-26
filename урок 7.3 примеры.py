# Дано число посчитать колиество нулей в нем
from random import randint

num = randint(99, 999999)
print(num)
count_zero = 0
for symbol in str(num):
    if symbol == 0:
        count_zero += 1
print(count_zero)
##  python style
print(str(num).count('0'))


## Дано целое число , определить количество нулей в конце числа. Например: 102034000 - 3 нуля
num = 102024000
print(num)
count_zero = 0
#
option1 = num
while num % 10 == 0:
    count_zero += 1
    num //= 10
print('option1', count_zero)
#
option2 = num
count_zero = 0
for sym in str(num)[::-1]:
    if sym == '0':
        count_zero += 1
    else:
        break
print('option2', count_zero)
#
option3 = num
count_zero = 0
for index in range(len(str(option3))-1, 0, -1):
    if str(option3)[index] == '0':
        count_zero += 1
    else:
        break
print('option3', count_zero)
## python style
option4 = num
print('len(str(option4)', len(str(option4)))  # узнал кол-во цифр получив строку
print('str(option4)[::-1]', str(option4)[::-1])  # переворот числа превращенного в строку
print('int(str(option4)[::-1]', int(str(option4)[::-1]))
print('len(str(int(str(option4)[::-1])))', len(str(int(str(option4)[::-1]))))  # превращение перевернутой строки в число
count_zero = len(str(option4)) - len(str(int(str(option4)[::-1])))  #вычитание одного из другого
print('option4', count_zero)
