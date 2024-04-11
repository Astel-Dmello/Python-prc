def number_to_words(number):
    # Define a dictionary to map digits to words
    digit_words = {
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
        '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
    }
    
    # Convert the number to a string and iterate over each digit
    words = [digit_words[digit] for digit in str(number)]
    
    # Join the words and return
    return ' '.join(words)

# Example usage:
number = 1234
words = number_to_words(number)
print(f"The number {number} in words is: {words}")
