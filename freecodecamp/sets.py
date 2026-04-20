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