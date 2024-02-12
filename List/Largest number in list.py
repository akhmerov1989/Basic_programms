numbers = [30, 20, -55, 3, 99]

minimum = numbers[0]

for i in numbers:
    if i > minimum:
        minimum = i

print("The smallest number in the list is:", minimum)

# Second-largest number in the list

numbers.sort(reverse=True)

if len(numbers) >= 2:
    second_largest = numbers[1]
    print("The second largest number in the list is: ", second_largest)
else:
    print("The list does not contain a second largest number.")
