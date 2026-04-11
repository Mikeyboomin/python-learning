motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Replacing elements in a list

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles[-1] = 'hyundai'
print(motorcycles)

# Adding elements to a list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)


cars = []

cars.append('porsche')
cars.append('rolls royce')
cars.append('ferarri')
cars.append('g-wagon')

print(cars)

# inserting elements into a list 

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

# removing elements from a list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Use the del statement if you know the position of the item you want to remove from a list

del motorcycles[0]
print(motorcycles)

# Removing an item using the pop() method
# The pop() method removes the last item in a list, but it lets you work with that item after removing it
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")


# Popping items from any position in the list

