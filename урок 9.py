'''
словарь = {ключ : значение} - ключ является неизменным объектом
'''

my_dict = {'key' : 'value'}
print(my_dict, type(my_dict))
##
address = {
           'city': 'kiev',
           'street': 'lesya kurbasa',
           'house': 25,
           'apartment': 33,
           14: 'четырнадцать'
}
person = {
    'name': 'volodimir',
    'age': 42,
    'address': address,
}
print(person)
print(person['name'])
print(person['address']['street'])
