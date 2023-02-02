try:
    divide_values = [2, 0, None, "1", True, False, [], {}]
    values_to_devide = [10, "1", None, True, False, [], 0, {}]
    for values in values_to_devide:
        for divide in divide_values:
            result = values / divide
            print(result)
except ZeroDivisionError:
    print('что-то пошло не так')
