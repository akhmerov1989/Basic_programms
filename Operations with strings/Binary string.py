def is_binary_string(input_str):
    # Iterate through each character in the inout string
    for i in input_str:
        if i not in '01':
            return False
    return True

input_str = "1001110"

if is_binary_string(input_str):
    print(f"'{input_str}' is a binary string")
else:
    print(f"'{input_str}' is not a binary string. ")
