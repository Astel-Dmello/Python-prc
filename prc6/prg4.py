def find_smallest_number(lst):
    if not lst:
        return None  # Return None if the list is empty
    min_number = lst[0]  # Initialize min_number with the first element of the list
    for num in lst[1:]:  # Iterate over the remaining elements in the list
        if num < min_number:
            min_number = num
    return min_number

# Example usage:
my_list = [10, 20, 4, 45, 99]
smallest_number = find_smallest_number(my_list)
print("The smallest number in the list is:", smallest_number)
