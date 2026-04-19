products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

"""
You write for, the loop variable (price in this case), products.values() to get all the values of the products
 dictionary, a colon, and then the body of the loop, where you can apply any logic to the values. In this case, 
 we are printing them.
"""

for price in products.values():
    print(price)

# And here is the output. As you can see, each value is printed to the console, one by one.

# You just need to iterate over products.keys() or products directly,  if you need to iterate over the keys of a dictionary.

for product in products.keys():
    print(product)

# Or

for product in products:
    print(product)

# And this works exactly the same for key-value pairs if you need to iterate over the keys 
# and their corresponding values simultaneously. 

for product in products.items():
    print(product)

"""
('Laptop', 990)
('Smartphone', 600)
('Tablet', 250)
('Headphones', 70)
"""    

# If you want to store the key and the value in separate loop variables, 
# you just need to define them and separate them with a comma.

for product, price in products.items():
    print(product, price)

"""
Laptop 990
Smartphone 600
Tablet 250
Headphones 70
"""    

#  If we want to offer a 20% discount, we would multiply each price by 0.8 
# and reassign it as the value of that product key.

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)

"""
Then, if we print the dictionary, we would get these key-value pairs with the discounted prices:

{
    'Laptop': 792, 
    'Smartphone': 480, 
    'Tablet': 200, 
    'Headphones': 56
}
"""

# if you need to iterate over the key-value pairs while keeping track of a counter, you can call the enumerate() function.

for product in enumerate(products):
    print(product)

# But the enumerate() function also assigns an integer to each key, so we get tuples with the integer and the key.
# 
# Here is the output:

# (0, 'Laptop')
# (1, 'Smartphone')
# (2, 'Tablet')
# (3, 'Headphones')   
# 
# If you need to, you can assign these values to separate loop variables.
# 
for index, product in enumerate(products):
    print(index, product)

# If you need to iterate over the values, you can replace products by products.values()
# 
for price in enumerate(products.values()):
    print(price)

"""
(0, 990)
(1, 600)
(2, 250)
(3, 70)
"""     

# You can assign them to separate loop variables as well:

for index, price in enumerate(products.values()):
    print(index, price)

# This will be the output. You can use them as you need to in your code:

# 0 990
# 1 600
# 2 250
# 3 70

# And with products.items(), you can get the entire key-value pair in addition to the "index" or "counter".

for index, product in enumerate(products.items()):
    print(index, product)

# we get the index followed by a tuple that contains the key and the value of the corresponding key-value pair
# 
# 0 ('Laptop', 990)
# 1 ('Smartphone', 600)
# 2 ('Tablet', 250)
# 3 ('Headphones', 70) 
# 
# To customize the initial value of the count, you can pass a second argument to enumerate(). 
# For example, here we are starting the count from 1   


for index, product in enumerate(products.items(), 1):
    print(index, product)

"""
You can see this change in the output. Now the first integer is 1 instead of 0:

1 ('Laptop', 990)
2 ('Smartphone', 600)
3 ('Tablet', 250)
4 ('Headphones', 70)
"""    