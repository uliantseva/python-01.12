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
print(age_min)
names_max_len = [person['name'] for person in persons if len(person['name']) > long_name]
print(names_max_len)
# с







