def find_repeated_items(tup):
    repeated_items = []
    for item in tup:
        if tup.count(item) > 1 and item not in repeated_items:
            repeated_items.append(item)
    return repeated_items

# Example usage:
my_tuple = (1, 2, 3, 4, 2, 3, 5, 6, 4)
repeated_items = find_repeated_items(my_tuple)
print("Repeated items in the tuple:", repeated_items)
