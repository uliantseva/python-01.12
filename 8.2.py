##5
my_str = 'abcde'
if len(my_str)%2!=0:
    my_str += "-"
li = []
for i in range(0, len(my_str), 2):
    li.append(my_str[i:i + 2])
print(li)


start_str = 'abcde'
li = [start_str[i:i + 2] for i in range(0, len(start_str), 2)]
if len(li[-1]) < 2:
    li[-1] += ' '
print(li)

## 6
li = [2, 4, 1, 5, 3, 9, 0, 7]
count = 0
for i in range(1, len(li) - 1):
    if li[i] > li[i - 1] + li[i + 1]:
        count += 1
print(count)
 #2 вариант
result = sum(1 for i in range(1, len(li) - 1)if li[i] > li[i - i] + li[i + i])
print(result)


## 7
li = [1, 2, 3, "11", "22", 33]
print([i for i in li if type(i) == str])
print([i for i in li if isinstance(i, str)])

