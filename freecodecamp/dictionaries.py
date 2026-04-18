# dictionaries in python work very similarly to real dictionaries, where you search for a word to find its corresponding meaning.
# With Python dictionaries, you use a key to find its corresponding value
# You should use dictionaries when you need to associate values to unique keys.

# This is the general syntax of a Python dictionary:

pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

# the dict() constructor builds the dictionary from a sequence of key-value pairs.

pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])

# To access the value of a key-value pair, you can write the name of the variable that holds the dictionary, 
# followed by square brackets, and the key you want to access within the square brackets:

pizza['name']

# This will evaluate to:

'Margherita Pizza'

# To update a value, you just need to add the assignment operator, followed by the new value.
# If the key doesn't exist in the dictionary, a new key-value pair will be created.

pizza['name'] = 'Margherita'

# Now the value of the key name is 'Margherita':

print(pizza['name']) # 'Margherita'

# METHODS used with dictionaries

# The .get() method retrieves the value associated with a key.
# It's similar to the bracket notation that we just used, but its advantage is that you can set a default value, 
# so you won't get an error if the key doesn't exist:

# In this example, if the toppings key doesn't exist, it will return an empty list, 
# which is the default value that we are passing here as the second argument.

pizza.get('toppings', []) # ['mozzarella', 'basil']

# The .keys() and .values() methods return a view object with all the keys and values in the dictionary, respectively:

pizza.keys()
# dict_keys(['name', 'price', 'calories_per_slice'])

pizza.values()
# dict_values(['Margherita Pizza', 8.9, 250])

# The .items() method returns a view object with all the key-value pairs in the dictionary, including both the keys and the values:

pizza.items()
# dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250)])

# The .clear() method removes all the key-value pairs from the dictionary:

pizza.clear()

"""
The .pop() method removes the key-value pair with the key that you specify as the first argument and returns its value. 
If the key doesn't exist, it returns the default value that you specify as the second argument. 
If the key doesn't exist and you don't pass a default value, a KeyError is raised:
"""

pizza.pop('price', 10)
pizza.pop('total_price') # KeyError

# In Python 3.7 and more recent versions, the .popitem() method removes the last inserted item:

pizza.popitem()

# finally, the .update() method updates the key-value pairs with the key-value pairs of another dictionary. 
# If they have keys in common, their values are overwritten.

pizza.update({ 'price': 15, 'total_time': 25 })

# In this example, we are updating the pizza dictionary. The price key exists in both of them, 
# so its value will be replaced with 15.

# But total_time is new, so it will be added to the pizza dictionary as a new key-value pair.

# result

{
    'name': 'Margherita Pizza', 
    'price': 15, 
    'calories_per_slice': 250, 
    'toppings': ['mozzarella', 'basil'], 
    'total_time': 25
}