from collections import Counter


def find_duplicates(input_str):
    # Count the occurrences of each character
    char_count = Counter(input_str)
    # Filter characters that occur more than once
    duplicates = [char for char, count in char_count.items() if count > 1]

    return duplicates


input_str = input("Enter a string: ")
duplicates_chars = find_duplicates(input_str)
print("Duplicate characters: ", duplicates_chars)


def find_duplicates(input_str):
    char_count = {}
    duplicates = []

    for i in input_str:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    for i, count in char_count.items():
        if count > 1:
            duplicates.append(i)

    return duplicates

input_str = "Sergey Akhmerov"
duplicates_chars = find_duplicates(input_str)
print("Duplicate characters: ", duplicates_chars)

