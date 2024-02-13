def remove_char(input_str, i):
    if i < 0 or i >= len(input_str):
        print(f"Invalid index {i}. The string remains unchanged.")
        return input_str

    # Remove the i-th character using slicing
    result_str = input_str[:i] + input_str[i+1:]

    return result_str

input_str = input("Enter a phrase: ")
i = int(input("Enter an index to remove: "))
new_str = remove_char(input_str, i)
print(f"Original string: {input_str}")
print(f"String after removing {i}th character : {new_str}")



