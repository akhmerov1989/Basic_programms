# Finding Sum of Array using Sum()
# Array in python is List
arr = [1, 2, 3]
sum_arr = sum(arr)
print("Sum of the array is ", sum_arr)


# Function to find the sum of elements in an array
def sum_of_array(arr):
    total = 0  # Initialize a variable to store the sum

    for element in arr:
        total += element  # Add each element to the total

    return total


# Example usage
array = [1, 2, 3]
result = sum_of_array(array)
print("Sum of the array: ", result)
