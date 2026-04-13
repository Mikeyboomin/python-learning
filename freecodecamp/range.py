# using range in a loop
for num in range(3):
    print(num) # 0 1 2

# if only one argument is passed, it is taken as the stop argument
# if two are passed range(1,2) first is taken as start and second as stop
# just like slicing lists, the stop is now included
# If a start argument is not specified, then the default is 0
# Otherwise, you can use the optional start argument to start the sequence of integers at a integer other than 0

for num in range(1, 5):
    print(num) # 1 2 3 4

# By default the sequence of integers will increment by 1
# But if you want to change that default, then you can use the optional step argument

for num in range(2, 11, 2):
    print(num) # 2 4 6 8 10

# you get a TypeError if you don't pass in the required stop argument
# the range function only accepts integers as valid arguments so no float

# If you want to generate a sequence of integers in decrementing order
# then you can use a negative integer for the step argument

for num1 in range(40, 0, -10):
    print(num1)

for num2 in range(10, 0, -1):
    print(num2)

# You can use the range function to create a list of integers using the list function

numbers = list(range(20, 1, -2))
print(numbers) # [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]

# The range() function is a very handy way to generate a sequence of integers in Python