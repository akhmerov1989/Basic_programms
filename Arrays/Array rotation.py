def rotate_array(arr, d):
    n = len(arr)

    # Check if 'd' is valid, it should be within the range of array length
    if d < 0 or d >= n:
        return "Invalid rotation value"

    # Create a new array to store the rotated elements.
    rotated_arr = [0] * n

    # Perform the rotation
    for i in range(n):
        rotated_arr[i] = arr[(i + d) % n]
    return rotated_arr


# Inout array
arr = [1, 2, 3, 4, 5]
# Number of positions to rotate
d = 2
# Call the rotate_array function
result = rotate_array(arr, d)

# Display
print("Original array: ", arr)
print("Rotated array: ", result)
