password = '123'
pass_in = input('Input password: ')
while pass_in != password:
    print('Wrong password: ')
    pass_in = input('try again: ')
else:
    print('Welcome')
##
password = '123'
count_try = 3
pass_in = input('Input password: ')
while pass_in != password:
    count_try -= 1
    if count_try == 0:
        print('No Welcome')
        break
    print('Wrong password: ')
    pass_in = input('try again: ')
else:
    print('Welcome')



# получить сумму всех цифр числа
num = int(input('input number'))
result = 0
while num > 0:
    result += num % 10   # result = result + num % 10
    num //= 10   # num = num // 10
print(result)

##
my_string = '0123456789'
for desytki in my_string:
    for edinitsi in my_string:             ## домашка но в цикле for
        result = int(desytki+edinitsi)
        print(result, end=' ')



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


columns=5
strings=5
for s in range(strings):
    for c in range(s + 1):
        print('*', end=' ')
print()



# D
h = int(input('Высота: '))
for i in range(2 * h + 1):
    if i <= h:
        print(' ' * (h - i) + '*' * (i + 1) + '*' * i)
    else:
        if i == (h * 2):
            print(' ' * h + '*')
        else:
            print(' ' * (i - h) + '*', end='')
            print(' ' * (2 * h - i - 1) + '*' + ' ' * (2 * h - i - 1) + '*')

