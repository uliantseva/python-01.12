simple_number = int(input('Введите число: '))
d = 0
for i in range(2, simple_number // 2+1):
    if simple_number % i == 0:
        d += d + 1
if d <= 0:
    print('Простое число')
else:
    print('Сложное число')








