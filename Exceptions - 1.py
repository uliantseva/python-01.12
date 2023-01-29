try:
    divide_values = [2, 0, None, "1", True, False, [], {}]
    values_to_devide = [10, "1", None, True, False, [], 0, {}]
    print(values_to_devide / divide_values)
except TypeError:
    print('Нельзя комбинировать эти типы данных')