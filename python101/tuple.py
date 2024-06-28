# s = {1, 2, 7, 9, 10, 3, 3, 3, 4, 4, 5, 8, 3, 0, }

# s.remove(3)
# print(s)

# dictionaries


my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict)

my_dict['country'] = 'USA' #adding a key value
print(my_dict)

my_dict['age']= '27' #overwriting the value
print(my_dict)

del my_dict['age'] #deleting key value
print(my_dict)

dictionary = {0: 'one', 1: 'two', 2: 'three'}
value = 0
for x in range(len(dictionary)):
  value = dictionary[x]
print(value)