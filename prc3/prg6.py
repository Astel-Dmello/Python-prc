def swap_variables(a, b):
    print("Before swapping:")
    print("a =", a)
    print("b =", b)
    # Swapping the values
    temp = a
    a = b
    b = temp
    print("\nAfter swapping:")
    print("a =", a)
    print("b =", b)
# Example usage
var1 = int(input("enter a number:"))
var2 = int(input("enter a number:"))
swap_variables(var1, var2)
