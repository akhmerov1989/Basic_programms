# Split a string into a list of words
input_str = input("Enter a string: ")
word_list = input_str.split() # By default

# Join the list
separator = "" # Specify the separator between words
output_str = separator.join(word_list)

print("Original string: ", input_str)
print("List if split words: ", word_list)
print("Joined string: ", output_str)
