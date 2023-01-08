persons = [
    {'name': 'John', 'age': 15},
    {'name': 'Katya', 'age': 24},
    {'name': 'Jack', 'age': 45},
    {'name': 'Masha', 'age': 20}
]
age_min = persons[0]['age']
for person in persons:
    if person['age'] < age_min:
        age_min = person['age']
print(age_min)



