# 1
persons = [
    {'name': 'John', 'age': 15},
    {'name': 'Katya', 'age': 24},
    {'name': 'Jack', 'age': 45},
    {'name': 'Masha', 'age': 20}
]
print('persons', persons)

# а)
age_min = persons[0]['age']
long_name = len(persons)
for person in persons:
    if person['age'] < age_min:
        age_min = person['age']
print('age_min', age_min)

# б)
names_max_len = [person['name'] for person in persons if len(person['name']) > long_name]
print('names_max_len', names_max_len)

# с)
#average = []
#for i in persons:
#    sum_age = int(sum('age'))
#    print(sum_age)

# 2
my_dict = {1: 2, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
print('my_dict', my_dict)
my_dict_2 = {0: 0, 1: 2, 6: 36, 8: 64, 9: 81, 16: 256}
print('my_dict_2', my_dict_2)

# a)
li = []
for key in sorted(my_dict.keys() & my_dict_2.keys()):
    li.append(key)
print('li', li)

# б)
li_2 = [key for key in my_dict if key not in my_dict_2]
print('li_2', li_2)

# в)
my_dict_3 = dict((key, my_dict[key]) for key in my_dict if key not in my_dict_2)
print('my_dict_3', my_dict_3)

# г)
keys = my_dict.keys() & my_dict_2
my_dict_4 = my_dict.copy()
my_dict_4.update(my_dict_2)
my_dict_4.update({key: [my_dict[key], my_dict_2[key]] for key in keys})
print('my_dict_4', my_dict_4)







