#question 2

def analyze_string(input_str):
    """Analyze the given string."""

    total_characters = 0
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    is_palindrome = False  # Initialize as False

    for char in input_str:
        total_characters += 1
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1

    # Corrected palindrome check
    reversed_str = input_str[::-1]
    if reversed_str.lower() == input_str.lower(): # != change to ==
        is_palindrome = True

    return total_characters, uppercase_count, lowercase_count, digit_count, is_palindrome


def main():
    try:
        # Get input from the user
        user_input = input("Enter a string: ")
        # Calculate and print the result
        result = analyze_string(user_input)
        print(f"Total characters: {result[0]}")
        print(f"Uppercase letters: {result[1]}")
        print(f"Lowercase letters: {result[2]}")
        print(f"Digits: {result[3]}")
        print(f"Palindrome: {'Yes' if result[4] else 'No'}")

    except Exception as e:  # Adjusted exception type
        print(f"Error: {e}")
        print("Please enter a valid string.")


if __name__ == "__main__":
    main()