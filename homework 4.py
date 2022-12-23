strings = 7
for s in range(1, strings + 1):
    for space in range(strings * 2 - s * 2):
        print(end=' ')
    for star in range(s * 2 - 1):
        print('*', end=' ')
    print()
#

strings = 7
for s in range(1, strings + 1):
    for space in range(1, strings - s + 1):
        print(end='  ')
    for star in range(1, 2 * s):
        if star == 1 or star == s * 2 - 1:
            print('*', end=' ')
        else:
            print('*', end=' ')
    print()
for i in range(strings - 1, 0, -1):
    for j in range(1, strings - i + 1):
        print(' ', end=' ')
    for star in range(1, 2 * i):
        if star == 1 or star == i * 2 - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#

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

#
strings = 7
for s in range(1, strings + 1):
    for space in range(1, strings - s + 1):
        print(end='  ')
    for star in range(1, 2 * s):
        if star == 1 or star == s * 2 - 1:
            print('*', end=' ')
        else:
            print('*', end=' ')
    print()
for i in range(strings - 1, 0, -1):
    for j in range(1, strings - i + 1):
        print(' ', end=' ')
    for star in range(1, 2 * i):
        if star == 1 or star == i * 2 - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    for k in range(1, strings - 6, 4):
        print('-', end=' ')
    print()






