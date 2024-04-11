import math

def calculate_area(radius):
    area = math.pi * radius ** 2
    return area

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_area(radius)
    circumference = calculate_circumference(radius)
    print("Area of the circle:", area)
    print("Circumference of the circle:", circumference)

if __name__ == "__main__":
    main()
