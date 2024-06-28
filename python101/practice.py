all = {'instructors': ['Ahmad', 'Abdul', 'Kris', 'Gulnaz', 'Esen'], 'members': ["Abdulhamid Abdullajonov", "Ahmadyar", "Aiya", "Esenbek", "Gulnaz", "Kris", "Marlen", "Meerim", "Mohammad", "Salmon", "Simon", "Abdul"]}

both =[]

for person in range(5):
    inst = all['instructors'][person]
    if inst in all['members']:
        both.append(inst)


print(both)