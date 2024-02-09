""" Disarium number is a number that is equal to the sum of its digits each raised to the power of its
 respective position. ( 89 = 8**1 + 9 **2 = 8 + 81)"""

def is_disarium(number):
    # Convert the number to a string to iterate over its digits
    num_str = str(number)

    # Calculation the sum
    digit_sum = sum(int(i)**(index + 1) for index, i in enumerate(num_str))

    # Check if the sum is equal to the original
    return digit_sum == number
# Input a number
try:
    num = int(input("Enter a number: "))

    # Check
    if is_disarium(num):
        print(f"{num} is a Disarium number.")
    else:
        print(f"{num} is not Disarium number.")
except ValueError:
    print("Invalid input. Please enter a valid numnber.")


# Print all disarium numbers between 1 and 100

disarium_numbers = [num for num in range(1,101) if is_disarium(num)]

print("Disarium numbers between 1 and 100:")
for num in disarium_numbers:
    print(num, end=" | ")



