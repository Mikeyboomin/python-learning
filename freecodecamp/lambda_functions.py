numbers = [1, 2, 3, 4, 5, 6]

def is_even(number):
    return number % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(even_numbers) # [2, 4, 6]

# lambda functions are anonymous functions, you don't have to call the name

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # [2, 4, 6]

# avoid writing complex lambda functions

