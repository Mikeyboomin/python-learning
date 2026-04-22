"""
In software development, a library is like a toolbox for developers.

Instead of having to implement every single part of the code yourself from scratch, a library gives you pre-written and reusable code, like functions, classes, and data structures that you can use in your projects.

Python has an extensive standard library with many different built-in modules. They're all standardized, well-vetted solutions for many of the problems and tasks you'll face daily as a programmer, such as:

Interacting with the operating system.

Working with files.

Networking.

Working with date and time.

Performing mathematical operations.

Using regular expressions.

Testing and debugging your code.

And much more!

Some examples of popular built-in modules are math, random, re (short for "regular expressions"), and datetime.

But how can you access the variables, constants, functions, and classes defined in these built-in modules?

You use an import statement. These statements let you import modules into your Python script. Import statements are generally written at the top of the file. Also, you can customize them based on your needs. First, you use the import statement, followed by the name of the module:
"""

import math

# Then, if you need to call a function from that module in your Python script, you would use dot notation, 
# with the name of the module followed by the name of the function

math.sqrt(36)

# this is the most basic version of an import statement, but there are other alternatives.

# if you need to import the module with a different name (also known as an "alias"), you can use this syntax, 
# with as followed by the alias at the end of the import statement

import math as m 

# then, you can access the elements of the module using the alias

m.sqrt(36)

# but sometimes you don't need to import everything from a module perhaps you only need one or two specific functions 
# or classes. Python has exactly what you need in that case

#  now the import statement starts with from, followed by the name of the module, 
# and then the import keyword followed by the name of the elements that you want to import

from math import radians, sin, cos

# Then, you can use these names without the module prefix in your Python script.

# if you want to assign aliases to these names, you can do that by using the as keyword after each, 
# followed by the alias you want to use

# now you can call these functions directly in your code, without the math module as a prefix

from math import radians, sin, cos

angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(sine_value) # 0.6427876096865393
print(cos_value)  # 0.766044443118978

# And finally, we find this import statement that ends with an asterisk. 
# The asterisk is telling Python that you want to import everything in that module, 
# but you want to import it so that you don't need to use the name of the module as a prefix

from math import *
print(sqrt(36))  # 6.0
print(pow(5, 2)) # 25.0
print(exp(1))    # 2.718281828459045

# However, this is generally discouraged because it can lead to namespace collisions, 
# and make it harder to know where certain names are coming from

# Import statements work exactly the same for functions, classes, constants, variables, 
# and any other elements defined in the module

import math
print(math.pi)

# and here is an example of a class from the datetime module
# we create a date object that represents July 15, 1959
# then, we assign that date object to a variable and access the day, month, 
# and year individually using dot notation

import datetime
birthday = datetime.date(1959, 7, 15)
print(birthday.day)    # 15
print(birthday.month)  # 7
print(birthday.year)   # 1959

# you should also know about this very important idiom in Python scripts, because they are very closely related

