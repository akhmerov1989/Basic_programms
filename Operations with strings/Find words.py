# Find words which are greater than given length k
def find_words(words, k):
    # Create an empty list to store words grater than k
    result = []

    # Iterate through each word in the list
    for i in words:
        if len(i) > k:
            result.append(i)

    return result


word_list = ["apple", "banana", "cherry", "dragon", "apple", "kiwi"]
k = int(input("Enter a length of characters: "))
long_words = find_words(word_list,k)
print(f"Words longer than {k} characters: {long_words}")


