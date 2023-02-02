try:
    person_data = {"name": "Bolt", "age": 23, "gender": "male", "born_date": "06.07.1990"}
    user_key = "email"
    print(person_data[user_key])
except KeyError:
    print('Такого ключа не существует')
finally:
    print('Жду следующий ключ')