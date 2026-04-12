# the append() method is used to add an item to the end of the list
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]

# you can also use the append() method if you want to add a list at the end of another list
numbers = [1, 2, 3, 4, 5]
complete_numbers = [6, 7, 8, 9, 10]
numbers.append(complete_numbers)
print(numbers) # [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]

# append nests lists into other lists instead of adding them as normal elements
# to add individual elements from one list to another you need to use the extend() method
numbers = [1, 2, 3, 4, 5]
complete_numbers = [6, 7, 8, 9, 10]
numbers.extend(complete_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# you can use the insert() method to insert an element at a specific index in a list
numbers = [1, 2, 3, 4, 5]
numbers.insert(4, 4.5)
print(numbers) # [1, 2, 3, 4, 4.5, 5]
del numbers[1]
print(numbers) # [1, 3, 4, 4.5, 5]

# you can use the remove() method to remove an element from a list
# it takes the value you want to remove as an argument
numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(50)
print(numbers) # [10, 20, 30, 40, 50]
# It is important to note that this method will only remove the first occurrence
#  of an item. Not all of them

numbers = [10, 20, 30, 40, 50, 50, 50]
numbers.remove(50)
print(numbers) # [10, 20, 30, 40, 50, 50]

# you can use the pop() method to remove an element at a specific index
numbers = [1, 2, 3, 4, 5]
numbers.pop(0) # The number 1 is returned
# If you don't specify an element for the pop method, then the last element is removed
numbers = [1, 2, 3, 4, 5]
numbers.pop()
print(numbers) # [1, 2, 3, 4]

# you can use the clear() method if you need to empty the list
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers) #[]

# the sort() method is used to sort the elements in place
numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()
print(numbers) # [1, 2, 19, 35, 41, 67]
# sorted() method is used to create a new sorted list from the old list without altering it
numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)
print(numbers) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]

# As a reminder, an iterable is a special type of object that you can loop over,
# allowing you to access each item one at a time.
# Both the sort() method and sorted() function accept optional key and reverse parameters.

# the reverse() method is used to reverse a list of elements in place
numbers = [1, 2, 3, 4, 5, 6]
numbers.reverse()
print(numbers) # [6, 5, 4, 3, 2, 1]

# the index method is used to find the first index where an element can be found in a list
programming_languages = ['Rust', 'Java', 'Python', 'C++']
print(programming_languages.index('Rust')) # 0

# If the element cannot be found, then Python throws a ValueError
# There are a few more methods for Python lists
# but this initial list of methods is a good place to start

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1::2])

one_to_five = [1, 2, 3, 4, 5]
six_to_ten = [6, 7, 8, 9, 10]
one_to_five.append(six_to_ten) # this actually alter the list
print(one_to_five)

one_to_five = [1, 2, 3, 4, 5]
six_to_ten = [6, 7, 8, 9, 10]
one_to_five.extend(six_to_ten) # this actually alter the list
print(one_to_five)

