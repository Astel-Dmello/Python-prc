def find_largest_number(lst):
    if not lst:
        return None  # Return None if the list is empty
    max_number = lst[0]  # Initialize max_number with the first element of the list
    for num in lst[1:]:  # Iterate over the remaining elements in the list
        if num > max_number:
            max_number = num
    return max_number

# Example usage:
my_list = [10, 20, 4, 45, 99]
largest_number = find_largest_number(my_list)
print("The largest number in the list is:", largest_number)
