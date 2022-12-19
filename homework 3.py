variable = input('Ввести знак операции:')
n1 = float(input('Введите число:'))
n2 = float(input('Введите число:'))
if variable == '+':
    print(n1+n2)
elif variable == '-':
    print(n1 - n2)
elif variable == '*':
    print(n1 * n2)
elif variable == '/':
    print(n1 / n2)
elif variable == '**':
    print(n1 ** n2)
else:
    print('Не указала знак операции')
    print('Не указала число операции')



N = int(input('введите ранг:'))
for i in range(1, int(N**0.5)+1):
    print(i**2, end=' ')
print()








