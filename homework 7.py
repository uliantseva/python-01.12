# 1
## а), б)
persons = [
    {'name': 'John', 'age': 15},
    {'name': 'Katya', 'age': 24},
    {'name': 'Jack', 'age': 45},
    {'name': 'Masha', 'age': 20}
]
age_min = persons[0]['age']
long_name = len(persons)
for person in persons:
    if person['age'] < age_min:
        age_min = person['age']
print('age_min', age_min)
for name in persons:
    if len(name['name']) > long_name:
        long_name = len(name['name'])
print('long_name', long_name)
# с
count = 0
for age in persons:
    sum_age = sum('age')
    count += 1
average = sum_age / count
print('The average of all the persons is:', average)





