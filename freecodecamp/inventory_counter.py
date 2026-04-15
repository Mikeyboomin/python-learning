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
    
    final_list.sort()  
    
    print(final_list)
    print(f"Total items: {len(final_list)}")
    return final_list  

inventory_counter(fruits)