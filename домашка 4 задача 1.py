my_string = '0123456789'
for k in my_string:
    for i in my_string:
        result = int(k+i)
        print(result, end=' : ')