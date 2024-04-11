def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

number1 = int(input("enter a number:"))
number2 = int(input("enter a number:"))
number3 = int(input("enter a number:"))

largest = find_largest(number1, number2, number3)
print("The largest number among", number1, ",", number2, ", and", number3, "is", largest)

