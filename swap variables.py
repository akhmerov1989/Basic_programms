# Input two variables
a = input("Enter the value of the 1 first variable (a): ")
b = input("Enter the value of the second variable (b): ")
# Display the original values
print(f"Original values: a = {a}, b = {b}")
# Swap the values ising a temporary variable
temp = a
a = b
b = temp
# Display the swapped values
print(f"Swapped values: a = {a}, b = {b}")


# Swap without temp variable

a = 5
b = 10

# Swapping
a,b = b,a
print(f"After swapping: a = {a},b = {b} ")
