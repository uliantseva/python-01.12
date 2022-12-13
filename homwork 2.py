n = int(input('количество школьников:'))
k = int(input('количество яблок:'))
print(f'остается яблок у каждого школьника {k//n}')
print(f'остается яблок в корзине {k%n}')


class1 = int(input('количество учеников:'))
class2 = int(input('количество учеников:'))
class3 = int(input('количество учеников:'))
print(f'количество парт для всех учеников {(class1+class2+class3)/2}')



num1 = int(input('введите число:'))
num2 = 0
while num1 > 0:
  digit = num1 % 10
  num1 = num1 // 10
  num2 = num2 * 10
  num2 = num2 + digit
print('"Обратное" ему число:', num2)









