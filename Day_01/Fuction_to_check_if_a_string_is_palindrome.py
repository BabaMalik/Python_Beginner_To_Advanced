original = input("Enter a string: ")
reverse= original[::-1]

if original == reverse:
    print("String is palindrome")
else:
    print("String is not palindrome")