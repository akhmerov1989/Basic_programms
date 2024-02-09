""" Happy number is positive integer that, when you repeatedly replace the number
 by the sum of the squares of its digits and continue the process, eventually reaches 1.
 19 is happy number
 1**2 + 9**2 = 82
 8**2 + 2**2 = 68
 6**2 + 8**2 = 100
 1**2 + 0**2 + 0**2 = 1"""


def is_happy_number(num):
    seen = set()  # to store previously seen numbers

    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(i) ** 2 for i in str(num))

    return num == 1


# Test the function
num = int(input("Enter a number: "))
if is_happy_number(num):
    print(f"{num} is happy number")
else:
    print(f"{num} is not a happy number")

# Print all happy numbers between 1 and 100
happy_numbers = [num for num in range(1, 101) if is_happy_number(num)]

print("Happy numbers between 1 and 100:")
for num in happy_numbers:
    print(num, end=" | ")
