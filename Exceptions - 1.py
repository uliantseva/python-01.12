try:
    divide_values = [2, 0, None, "1", True, False, [], {}]
    values_to_devide = [10, "1", None, True, False, [], 0, {}]
    for values in values_to_devide:
        for devide in divide_values:
            result = values /devide
            print(result)
except ZeroDivisionError:
    print('Делить на ноль нельзя')










