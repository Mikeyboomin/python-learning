# count() method is used to determine how many times an item appears in a tuple
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(programming_languages.count('Rust')) # 2

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(programming_languages.count('Go')) # 0
# if no arguments are passed, it returns a TypeError

# the index() methos is method is used to find the index where a particular item is present in a tuple
# it takes a value as an argument
print(programming_languages.index('Rust')) # 0

# if the specified item cannot be found, then Python raises a ValueError
# another thing you can do with the index() method is to pass in optional 
# start and stop index arguments

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
programming_languages.index('Python', 3) # 5 (this starts the search at the third element 
# and only retuns the python elementa after it)

# you can also specify a stop  index
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
print(programming_languages.index('Python', 2, 5)) # 2
print(programming_languages.index('Python', 2, 6))

# the sorted() function will always create a new list of the sorted values
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
sorted_programming_languages = sorted(programming_languages)
print(sorted_programming_languages)

# if you need to customize the sorting behavior for an iterable
# you can use the optional reverse and key arguments
# here is an example of using key argument to sort items in a tuple by length
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(programming_languages, key=len)) # ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']
# you can't use the sort method for tuples because they are immutable

# if you want to create a new list of values in reverse order
# then you can use the reverse argument like this
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(programming_languages, reverse=True)) # 


# sorting a list of tuples
list_of_tuples = [(1, 2, 3, 4, 5), (2, 3, 4, 5, 6), (1, 2, 4, 6, 7)]
print(list_of_tuples)
list_of_tuples.sort()
print(list_of_tuples)