# Count how many times each fruit appears.

# Build a new list that repeats each fruit according to that count.

# Print the list and the total count.

fruits = "apple,banana,apple,orange,banana,grape,banana"

def inventory_counter(inventory):
    inventory_list = inventory.split(',')
    unique_items = []
    final_list = []

    for item in inventory_list:
        if item not in unique_items:
            unique_items.append(item)
            count = inventory_list.count(item)
            final_list.extend([item] * count) 

            final_list.sort()  # optional, but matches example output
    
    print(f"Total items: {len(final_list)}")
    return final_list  

  

print(inventory_counter(fruits))


# I have been able to get the count of each items, i need to add each item to the list the amount of times 
# they appear in inventory_list

# I have to split the strings by a comma and turn them into a new list of items seperated by comma
# I also have to create a new list that stores the new items according to the number of items they appeared
# on the previous list
# meaning that I have to count each unique items
# Then I have to count the total number of items on the final list and output it