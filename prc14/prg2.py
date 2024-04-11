class AreaCalculator:
    def area_rectangle(self, length, breadth):
        area = length * breadth
        print("Area of rectangle:", area)

    def area_square(self, side):
        area = side ** 2
        print("Area of square:", area)

# Example usage:
obj = AreaCalculator()

# Calculate and print the area of a rectangle
obj.area_rectangle(5, 10)

# Calculate and print the area of a square
obj.area_square(7)
