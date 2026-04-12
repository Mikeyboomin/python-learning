# accessing the first element in a list
cities = ['Los Angeles', 'London', 'Tokyo']
print(cities[0])

# accessing the last element in a list
cities = ['Los Angeles', 'London', 'Tokyo']
print(cities[-1])

# you can use a list() constructor to also make a list from an iterable
name = 'jessica'
print(list(name)) # ['j', 'e', 's', 's', 'i', 'c', 'a']

# an iterable is a special type of object that can be looped over one item at a time.
# you can use the len() function to get the total number of elements in a list

numbers = [1, 3, 3, 4, 5]
print(len(numbers)) # 5

# replacing elements in a list
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[1] = 'Go'
print(programming_languages) # ['Python', 'Go', 'C++', 'Rust']

# Since lists are mutable, you can update any element in the list as long 
# as you pass in a valid index number. If you pass in an index (either positive or negative)
#  that is out of bounds for the list, then you will receive an IndexError

# If you want to remove an element from a list permanently you can use del()
programming_languages = ['Python', 'Java', 'C++', 'Rust']
del programming_languages[1]
print(programming_languages)

# to check if an element is inside the list you can use the in keyword like this:
programming_languages = ['Python', 'Java', 'C++', 'Rust']
print('Python' in programming_languages) # True
print('php' in programming_languages) # False
del programming_languages[2]
del programming_languages[0]
print(programming_languages)

# It's common to have nested lists
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]

# you still access nested lists like you do other lists
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
print(developer[2]) # ['Python', 'Rust', 'C++']

# to access the second language from that nested list:
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
print(developer[2][1]) # Rust

# unpacking values from a list is basically assigning elements on a list to variables
developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer
print(name) # Alice
print(age) # 34
print(job) # Rust Developer

# If you need to collect any remaining elements from a list
# you can use the asterisk (*) operator
developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer
print(name) # Alice
print(rest) # [34, 'Rust Developer']

# If the numbers of variables on the left side of the assignment operator 
# doesn't match the total numbers of items in the list, then you will receive a ValueError
developer = ['Alice', 34, 'Rust Developer']
# name, age, job, city = developer # ValueError: not enough values to unpack (expected 4, got 3)

# You can slice part of the string to retrieve some elements
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies'] 
# slices from start to exclude end
print(desserts[0:3]) # ['Cake', 'Cookies', 'Ice Cream']

# you can specify a step interval which determines how much to increment between the indices
# for example if you need to slice even numbers from this string
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1::2]) # 2, 4, 6, 8, 10
# slices from 2 and skips the next and so on
