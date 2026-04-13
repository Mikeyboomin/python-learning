# Given a list of names, print each one with its position number starting from 1

names = ['Tessa', 'Angel', 'Nneka', 'Ifeoma', 'Francisca']

for count_names, name in enumerate(names, 1):
    print(f'number {count_names} and name {name}')


# Using enumerate to index lists
cars = ['benz', 'bmw', 'aston martin', 'ferrari']

for index, car in enumerate(cars, 2):
    print(f'index is {index} and car is {car}')

# using zip() to iterate over multiple lists
student = ['Naomi', 'Steven', 'Aaron', 'Adam', 'Lisa']
ids = ['001', '002', '003', '004', '005']

for name, id in zip(student, ids):
    print(f'Student Name: {name}')
    print(f'Student ID: {id}')


names = ['Tessa', 'Angel', 'Nneka', 'Ifeoma', 'Francisca', 'fly']

for name in names:
    for letter in name:
        if letter in 'aeiou':
            print(f'{letter} is a vowel and is in {name}')
            break
    else:
        print(f'{name} does not have a vowel in it!')        