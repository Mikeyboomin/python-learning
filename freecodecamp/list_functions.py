even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

# store odd numbers into an empty list called odd numbers

odd_numbers = []

for num in range(20):
    if num % 2 != 0:
        odd_numbers.append(num)

print(odd_numbers)


odd_numbers = [num for num in range(20) if num % 2 != 0]
print(odd_numbers)

numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)

# Another way to create a list starting from an existing iterable is the filter() function

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words)

"""
another function to be aware of is the map() function, which takes an iterable and applies 
a function to each of its elements. Here is an example of using the map() function to convert 
a list of temperatures from Celsius to Fahrenheit
"""

celsius = [0, 10, 20, 30, 40]

def fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(fahrenheit, celsius))
print(fahrenheit)

# just like the filter() function, map() accepts a function and an iterable for its arguments.
# the sum function is used to get the sum from an iterable like a list or tuple

numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total) # Result: 50

# you can also pass in an optional start argument which sets the initial value for the summation

numbers = [5, 10, 15, 20]
total = sum(numbers, 10) # positional argument which assumes youre starting the summation from 10 instead of 0
print(total) # 60

# you can also choose to use the start argument as a keyword argument

numbers = [5, 10, 15, 20]
total = sum(numbers, start=10) # keyword argument
print(total) # 60