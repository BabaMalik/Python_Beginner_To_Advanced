import re
def reverse_sentence_and_words(sentence):
    # Step 1: Split the sentence into words and punctuation, preserving order
    words = re.findall(r'\w+|\S', sentence)

    # Step 2: Reverse the order of words in the sentence
    reversed_order = words[::-1]

    # Step 3: Reverse each word individually
    reversed_each_word = [word[::-1] for word in reversed_order]

    # Step 4: Adjust the final output to include spaces properly
    # Use regex to add a space between words but not between a word and punctuation
    final_sentence = ' '.join(reversed_each_word)
    final_sentence = re.sub(r'\s+([,.!?;])', r'\1', final_sentence)

    return final_sentence


# Example usage
sentence = "Hello, world. How are you?"
result = reverse_sentence_and_words(sentence)
print(result)

