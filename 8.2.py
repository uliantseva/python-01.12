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
