#cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Boston']
#print(cities[3])
#print(cities[-1])
#print(cities[3:])

#print('cities')



# cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
# for index in range(len(cities)):
#     print("Current index: ", index, '| Current city: ', cities[index])


# cities = []

# while len(cities) <= 5:
#     user_input = input("Please enter city name: ")
#     if user_input in cities:
#         print ("City already exists:", user_input)
#         continue
#     else:
#         cities.append(user_input)
# print(len(cities), cities)


# cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
# cities[0], cities[4] = cities[4], cities[0]
# print(cities)

# Answer: ['Phoenix', 'Los Angeles', 'Chicago', 'Huston', 'New York']


# spendings = [32.45, 18.65, 23.45, 78.32, 5.23]

# sum = 0.0
# for spending in spendings:
#     sum += spending
# print('Money spent:', sum)

# spendings.sort(reverse=True)
# print(spendings)

# original_list = [1, 2, 3, 4, 5]
# new_list = original_list.copy()

# new_list.append(6)
# print(new_list)
# print(original_list)

###list-comprehension

#new_list = [expression for item in iterable]

# squares =[i**2 for i in range(1, 11)]
# print(squares)


squares =[i**2 for i in range(1, 11) if i % 2 == 0]
print(squares)

squares =[]
for i in range(1, 11):
    if i % 2 == 0:
        squares.append(i**2)
print(squares)
