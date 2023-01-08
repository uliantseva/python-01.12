# 1
strings = 7
for s in range(1, strings + 1):
    for space in range(strings * 2 - s * 2):
        print(end=' ')
    for star in range(s * 2 - 1):
        print('*', end=' ')
    print()
# 2
strings = 7
for s in range(1, strings + 1):
    for space in range(strings * 2 - s * 2):
        print(end=' ')
    for star in range(2 * s - 1):
        if star == 0 or star == s * 2 - 2:
            print('*', end=' ')
        else:
            if s == strings:
                print('*', end=' ')
            else:
                print(' ', end=' ')
    print()
# 3
strings = 7
count = -1
for s in range(1, strings * 2):
    print(s, end=' ->\t')
    if s < strings + 1:
        count += 2
    else:
        count -= 2
    for space in range(count, strings * 2 - 1):
        print(' ', end='')
    for star in range(count):
        if s <= strings or star == 0 or star == count - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
# 3
strings = 7
count = -1
for s in range(1, strings * 2):
    print(s, end=' ->\t')
    if s < strings + 1:
        count += 2
    else:
        count -= 2
    for space in range(count, strings * 2 - 1):
        print(' ', end='')
    for star in range(count):
        if s <= strings or star == 0 or star == count - 1 or star == count // 2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#


my_string = '0123456789'
i = 0
while i < 100:
    print(i, end=' : ')
    i += 1

