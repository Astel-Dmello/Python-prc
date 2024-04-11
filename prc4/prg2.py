def absolute_value(number):
    if number >= 0:
        return number
    else:
        return -number

# Example usage
input_number = -5
absolute = absolute_value(input_number)
print("The absolute value of", input_number, "is", absolute)
