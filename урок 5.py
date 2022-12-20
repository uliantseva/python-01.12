# получить сумму всех цифр числа
num = int(input('input number'))
result = 0
while num > 0:
    result += num % 10   # result = result + num
    num //= 10   # num = num // 10
print(result)



# цикл в цикле
sym_in_string = 5
count_of_strings = 4
for h in range(count_of_strings):
 for w in range(sym_in_string):
    print('*', end=' ')
 print()



 columns=5
 strings=5
 for s in range(strings):
     for c in range(columns):
         print('*', end=' ')
     print()


olumns=5
strings=5
for s in range(strings):
     for c in range(s + 1):
         print('*', end=' ')
     print()

