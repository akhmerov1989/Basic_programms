# define punctuation
punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''

# To take input from the user
my_str = input("Enter a string: ")

# remove punctuaton from the string
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char

# Display
print(no_punct)
