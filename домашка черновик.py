



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




