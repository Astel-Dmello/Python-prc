def find_min_max_numbers(tuple):
    min_number = min(tuple)
    max_number = max(tuple)
    return min_number, max_number

# Example usage:
my_tuple = (10, 20, 4, 45, 99)
min_number, max_number = find_min_max_numbers(my_tuple)
print("Minimum number in the tuple:", min_number)
print("Maximum number in the tuple:", max_number)
