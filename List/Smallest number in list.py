numbers = [30, 20, -55, 3, 99]

minimum = numbers[0]

for i in numbers:
    if i < minimum:
        minimum = i

print("The smallest number in the list is:", minimum)
