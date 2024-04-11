class PrintIntegerAndCharacter:
    def print_int_char(self, n, c):
        print("Integer:", n)
        print("Character:", c)

    def print_char_int(self, c, n):
        print("Character:", c)
        print("Integer:", n)

# Example usage:
obj = PrintIntegerAndCharacter()

# Call the first method with integer first and then character
obj.print_int_char(5, 'A')

# Call the second method with character first and then integer
obj.print_char_int('B', 10)
