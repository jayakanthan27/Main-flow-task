def count_words(sentence):
    words = sentence.split()  # Split the sentence into words
    return len(words)  # Return the number of words

# Example usage
sentence = "This is a simple sentence."
print("Number of words:", count_words(sentence))
