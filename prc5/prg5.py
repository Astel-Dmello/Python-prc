def is_palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]
num = int(input("enter ="))
if is_palindrome(num):
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
