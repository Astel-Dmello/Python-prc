def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

number = int(input("Enter a number: "))
result = check_number(number)
print("The number", number, "is", result)

