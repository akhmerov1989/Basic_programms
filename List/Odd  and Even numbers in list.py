numbers = [1,2,3,4,5,6,7,8,9]

even_numbers = [num for num in numbers if num % 2 == 0]

print("Even numbers in the list: ", even_numbers)

odd_numbers = [num for num in numbers if num % 2 != 0]

print("Odd numbers in the list: ", odd_numbers)
