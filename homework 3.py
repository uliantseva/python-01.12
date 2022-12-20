n1 = float(input('Введите число: '))
symbol = input('Ввести знак операции: ')
n2 = float(input('Введите число: '))
if symbol == '+':
    print(n1 + n2)
elif symbol == '-':
    print(n1 - n2)
elif symbol == '*':
    print(n1 * n2)
elif symbol == '/':
    print(n1 / n2)
elif symbol == '**':
    print(n1 ** n2)
else:
    print('Не указала знак операции')
    print('Не указала число операции')

#

N = int(input('Введите ранг: '))
for i in range(1, int(N**0.5)+1):
    print(i**2, end=' ')

#

simple_number = int(input('\nВведите число: '))
d = 0
for i in range(2, simple_number // 2+1):
    if simple_number % i == 0:
        d += d + 1
if d <= 0:
    print('Простое число')
else:
    print('Сложное число')












