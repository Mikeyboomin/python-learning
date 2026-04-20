# sets a built in data structures in python that can't have the same values, 
# they are also mutable meaning their contents can be changed and thay and unordered 
# meaning you can't access them with indicies

# They can only contain values of immutable data types like numbers, strings, and tuples
# and they support mathematical set operations, including union, intersection, difference, and symmetric difference

my_set = {1, 2, 3, 4, 5} 
even_set = {2, 4, 6, 8, 10}

# when defining an empty set you must always use the set() function, 
# if you use the empty curly braces ({}) python creates a dicytionary

# you can add an element to a set with the .add() method, and pass in the new element as argument.

even_set.add(12)
print(even_set) # {2, 4, 6, 8, 10, 12}

# if you try to add an element that is already in the set, only one will be kept

even_set.add(4) 
print(even_set) # {2, 4, 6, 8, 10, 12}

# you can either use the .remove() method or the .discard() method to remove an element from the set
# then pass  in the element you want to remove as an argument
# the .remove() method will raise a KeyError if the element is not found, while the .discard() method will not

even_set.remove(4)
even_set.discard(4)

# the .clear() method removes all the elements from the set

even_set.clear()

# python sets also have powerful methods that perform common mathematical set operations
# the .issubset() and the .issuperset() methods check if a set is a subset or superset of another set, respectively

"""
here, we are checking if your_set is a subset of my_set, 
which is False because not all the elements of your_set are in my_set

we are also checking if my_set is a superset of your_set 
this is also False because my_set does not have all the elements of your_set
"""

my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set)) # False
print(my_set.issuperset(your_set)) # False

# the .isdisjoint() method checks if two sets are disjoint, which means they don't have any elements in common
# in this case, that's False because my_set and your_set do have common elements – 2, 3, and 4

print(my_set.isdisjoint(your_set)) # False

# the union operator | returns a new set with all the elements from both sets

print(my_set | your_set) # {1, 2, 3, 4, 5, 6}

# the intersection operator & returns a new set with only the elements that the sets have in common

print(my_set & your_set) # {2, 3, 4}

# the difference operator - returns a new set with the elements of the first set 
# that are not in the other sets. In this example, the numbers 1 and 5 are in my_set but NOT in your_set

print(my_set - your_set) # {1, 5}

# the symmetric difference operator ^ returns a new set with the elements that are either 
# in the first or the second set, but not both
# in this case, 1 and 5 are in my_set but not in your_set, so they are included
# and the number 6 is in your_set but not in my_set, so it's included as well

print(my_set ^ your_set) # {1, 5, 6}

# each one of these operators also has its corresponding compound assignment operator 
# if you add the equal sign next to it 
# these operators automatically assign the resulting set to the first set in the expression

# |= &= -= ^=

# for example, the -= operator finds the difference between the sets and updates the first set with that result

my_set -= your_set

print(my_set)

# you can check if an element is in a set or not with the in operator
# here, we are checking if 5 is in my_set
# the result will be a boolean value True or False

print(5 in my_set)