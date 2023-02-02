try:
    divide_values = [2, 0, None, "1", True, False, [], {}]
    values_to_devide = [10, "1", None, True, False, [], 0, {}]
    result = values_to_devide / divide_values
    print(result)
except TypeError:
    print('Нельзя комбинировать эти типы данных')










