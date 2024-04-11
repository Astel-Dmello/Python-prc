def multiply_list(lst):
    result = 1
    for item in lst:
        result *= item
    return result

# Example usage:
my_list = [1, 2, 3, 4, 5]
result = multiply_list(my_list)
print("The result of multiplying all items in the list is:", result)
