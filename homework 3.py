n1 = float(input('Введите число:'))
symbol = input('Ввести знак операции:')
n2 = float(input('Введите число:'))
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



N = int(input('Введите ранг:'))
for i in range(1, int(N**0.5)+1):
    print(i**2, end=' ')












