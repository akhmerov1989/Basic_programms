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


# N largest elements in the list
def find_n_largest_elements(lst, n):
    sorted_lst = sorted(lst, reverse=True)
    # Get the first N elements
    largest_elements = sorted_lst[:n]
    return largest_elements


numbers = [30, 10, 340, 56, 76, 7, 8, 4, 6, 5, 65, 708]

N = int(input("N = "))
result = find_n_largest_elements(numbers, N)
print(f"THe {N} largest elements in the list are: ", result)


