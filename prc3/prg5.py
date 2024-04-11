def calculate_area(side_length):
    return side_length * side_length

def calculate_perimeter(side_length):
    return 4 * side_length

# Example usage:
side_length = float(input("Enter the length of a side of the square: "))

area = calculate_area(side_length)
perimeter = calculate_perimeter(side_length)

print("The area of the square is:", area)
print("The perimeter of the square is:", perimeter)
