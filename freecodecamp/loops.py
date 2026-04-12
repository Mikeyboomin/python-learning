# loops are used to repeat a block of code for a set number of times
# The first loop we will go over is the for loop
programming_languages = ['Rust', 'Java', 'Python', 'C++']
for language in programming_languages:
    print(language) #Rust Java Python C++
# the block of code within the loop has to be indented or you get an error

# you can also use a for loop to iterate through other iterables like a string
for char in 'code':
    print(char) # c o d e

# you can also nest for loops in Python
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)

"""
The outer loop will iterate through each category in the categories list. 
For each category, the inner loop will iterate through each food in the foods list. 
Here is the result that will be printed to the console

Fruit Apple
Fruit Carrot
Fruit Banana
Vegetable Apple
Vegetable Carrot
Vegetable Banana
"""

genders = ['male', 'female']
names = ['Alice', 'John', 'Michael', 'Theresa']

for gender in genders:
    for name in names:
        print(gender, name)

# another type of loop you can use in Python is the while loop
# this type of loop will repeat a block of code until the condition is False
secret_number = 5
guess = 0

while guess != secret_number:
    guess = int(input("Guess my secret number "))
    if guess != secret_number:
        print("Wrong guess, try again!")
    else:
        print("You got it right!")

# the break statement is used to stop the execution of a loop
developers = ['Tessa', 'Jessica', 'Amie']

for developer in developers:
    if developer == 'Jessica':
        break
    print(developer)

# we iterated through a list of developers and print each name to the console
# if the name is equal to Naomi, then we break out of the loop
# this results in only the name Jess being printed to the console

# he continue statement is used to skip the current iteration of a loop 
# and move onto the next iteration
developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer) # Jess Tom

"""
Now the result in the console will be different
The names Jess and Tom are printed because the continue statement skips 
the second iteration of the loop when developer is equal to Naomi, 
and does not print that name to the console.
"""

words = ['milla', 'tessa', 'fly', 'avocado']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f'{word} contains vowel {letter}')
            break
    else:
        print(f'{word} has no vowels')

"""
we have a list of random words, and a for loop is used to loop through each word. 
Inside the outer for loop, we have another for loop to loop through each letter of each word.
If the lowercase version of the letter is a vowel, we print the word followed by what vowels 
it contains, then break out of the inner loop. If the word contains no vowels, then we print a
 message indicating that.
"""

# both for and while loops can be combined with an else clause, which is executed only when the 
# loop is not terminated by a break statement.