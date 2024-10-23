def first_non_repeating_character(s):
    # Create a dictionary to count occurrences of each character
    char_count = {}

    # Count each character in the string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char

    return None  # Return None if there are no non-repeating characters


# Example usage
input_string = input("Enter a string: ")
result = first_non_repeating_character(input_string)

if result:
    print(f"The first non-repeating character is: '{result}'")
else:
    print("There are no non-repeating characters.")