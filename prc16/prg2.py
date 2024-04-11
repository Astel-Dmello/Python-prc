class IncorrectPasswordError(Exception):
    pass

def validate_password(password):
    correct_password = "password123"  # Example correct password

    if password != correct_password:
        raise IncorrectPasswordError("Incorrect password!")

# Example usage:
try:
    password_input = input("Enter password: ")
    validate_password(password_input)
    print("Password is correct.")
except IncorrectPasswordError as e:
    print(e)
