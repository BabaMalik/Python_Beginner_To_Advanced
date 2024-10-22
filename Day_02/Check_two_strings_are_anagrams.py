# Using Character Counting
# This method manually counts the occurrences of each character using a list.


def are_anagrams(str1, str2):
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Check if lengths are different
    if len(str1) != len(str2):
        return False

    # Create a count array for characters
    count = [0] * 26  # Assuming only lowercase letters a-z

    for char in str1:
        count[ord(char) - ord('a')] += 1

    for char in str2:
        count[ord(char) - ord('a')] -= 1

        # If any count goes negative, they aren't anagrams
        if count[ord(char) - ord('a')] < 0:
            return False

    return True


# Example usage
string1 = "Listening"
string2 = "Silent"
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")