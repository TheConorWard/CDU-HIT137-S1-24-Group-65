#Chapter 2 - Question 2

def separate_and_convert(input_string):
    letters = []
    numbers = []

    for char in input_string:
        if char.isalpha():
            letters.append(char)
        elif char.isdigit():
            numbers.append(int(char))

    letters_ascii = [ord(char) for char in letters if char.isupper()]
    numbers_ascii = [num if num % 2 == 0 else num for num in numbers]

    return letters_ascii, numbers_ascii

# Example usage
input_string = "aBcDeF12345678GhIjK"
letters_ascii, numbers_ascii = separate_and_convert(input_string)
print("ASCII values of uppercase letters:", letters_ascii)
print("Even numbers:", numbers_ascii)
