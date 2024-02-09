""" Harshad number is an integer that is divisible by the sum of its digits.
18 = 1 + 8, 18 / 9"""


def is_harshad_number(num):
    # Calculate the sum of the digits of the number
    digit_sum = sum(int(i) for i in str(num))

    # Check if the number is divisible by the sum of its digits
    return num % digit_sum == 0


# Input a number
num = int(input("Enter a number: "))

# Check if it's a Harshad number
if is_harshad_number(num):
    print(f"{num} is  Harshad number.")
else:
    print(f"{num} is not Harshad number.")


