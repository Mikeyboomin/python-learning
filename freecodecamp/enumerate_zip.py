# previously learnt how to repeat a block of code several times
languages = ['Spanish', 'English', 'Russian', 'Chinese']

for language in languages:
    print(language)

# what if you wanted to keep track of the index for each element? 
languages = ['Spanish', 'English', 'Russian', 'Chinese']
index = 0

for language in languages:
    print(f'index {index} contains language {language}')
    index += 1

# that works but an easier way to do that is by using the enumerate() function
# the enumerate() function keeps track of the index for an iterable and returns an enumerate object
# If we pass the languages list to the enumerate() function and convert its returned value into 
# a list with the list() function it looks like this:

languages = ['Spanish', 'English', 'Russian', 'Chinese']

print(list(enumerate(languages)))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

# To refractor the code from earlier

languages = ['Spanish', 'English', 'Russian', 'Chinese']

for count, language in enumerate(languages):
    print(f'count {count} and language {language}')

languages = ['Spanish', 'English', 'Russian', 'Chinese']

for pair in enumerate(languages):
    print(pair)

# The enumerate() function also accepts an optional start argument that specifies the starting value for the count
# If this argument is omitted, then the count will begin at 0

# Given a list of names, print each one with its position number starting from 1

names = ['Tessa', 'Angel', 'Nneka', 'Ifeoma', 'Francisca']

for count_names, name in enumerate(names, 1): # counting starts at 1 instead of 0
    print(f'number {count_names} and name {name}') 

# So far we've only been iterating over one list. But what if you need to iterate over multiple iterables in parallel?
# zip() function combines lists into pairs of elements and returns an iterator of tuples

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

print(list(zip(developers, ids)))

# here's an example of using the zip() function with a for loop to iterate over developers and ids
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')

