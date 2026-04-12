# tuples are a data type used to create an ordered sequence of values
developer = ('Alice', 24, 'Rust Developer')
# unlike lists, tuples are immutable
# If you try to update one of the items in the tuple, you will get a TypeError

# to access an element from a tuple, you can use bracket notation and the index number
developer = ('Alice', 24, 'Rust Developer')
print(developer[2]) # Rust Developer

# if you need to access elements starting from the end of a tuple
# then you can use negative indexing
developer = ('Alice', 24, 'Rust Developer')
print(developer[-2]) # 24

# If you try to pass in an index number that exceeds or equals the length of the tuple
# you will receive an IndexError like this
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# you can also create a tuple is by using the built in tuple() function
name = 'Jessica'
print(tuple(name)) # ('J', 'e', 's', 's', 'i', 'c', 'a')

# to check if an item is in a tuple, you can use the in keyword like this
developer = ('Alice', 24, 'Rust Developer')
print('Alice' in developer)

# you can also unpack items from a tuple just like with lists
developer = ('Alice', 24, 'Rust Developer')
name, age, job = developer
print(name) # Alice
print(age) # 24
print(job) # Rust Developer

# you can use the asterisk * operator to collect any remaining elements from a tuple
developer = ('Alice', 24, 'Rust Developer')
name, *others = developer
print(name) # Alice
print(others) # [24, 'Rust Developer']

# you can use the slice operator on a tuple to extract a portion of it
developer = ('Alice', 24, 'Rust Developer')
print(developer[0:2]) # ('Alice', 24)
print(developer[0::2]) # ('Alice', 'Rust Developer')

# it's not possible to remove elements from a tuple because they are immutable 
del developer[1] # TypeError: "tuple" object doesn't support item deletion

"""
If you need a dynamic collection of elements where you can add, remove and update elements, 
then you should use a list. If you know that you are working with a fixed and immutable 
collection of data, then you should use a tuple.
"""