# Словари

my_dict = {'Yury': 1989, 'Sveta': 1981, 'Casper': 2023}
print(my_dict)
print(my_dict['Yury'])
print(my_dict.get('Kisya', 'Отсутствует ключ'))
my_dict.update({'Ira': 2004, 'Eugene': 1988})
print(my_dict)
casper = my_dict.pop('Casper')
print(casper)
print(my_dict)

# Множества

my_set = {1989, 1981, 'Casper-Dog', 'Good niece', False}
print(my_set)
my_set.add('Independent niece')
my_set.add(2004)
print(my_set)
my_set.discard(False)
print(my_set)
