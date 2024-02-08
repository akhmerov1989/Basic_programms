# Program to sort alphabetically the words

my_str = input("Enter a string: ")

# breakdown the sting into a ;ist of words
words = [word.capitalize() for word in my_str.split()]

# sort the list
words.sort()
# desc order
# words.sort(reverse=True)

# display the sorted words
print("The sorted words are:")
for word in words:
    print(word)
