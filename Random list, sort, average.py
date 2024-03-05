import random

def generate_random_list(size, min_value, max_value):
    # Generate a random list of integers
    random_list = [random.randint(min_value, max_value) for _ in range(size)]
    return random_list

def calculate_sum(numbers):
    # Calculate the sum of a list of numbers
    return sum(numbers)

def calculate_average(numbers):
    # Calculate the average of a list of numbers
    return sum(numbers) / len(numbers)

def main():
    # Generate a random list of integers
    size = 10
    min_value = 1
    max_value = 100
    random_list = generate_random_list(size, min_value, max_value)

    # Sort the list in ascending order
    sorted_list = sorted(random_list)

    # Calculate the sum of the list
    total_sum = calculate_sum(sorted_list)

    # Calculate the average of the list
    average = calculate_average(sorted_list)

    # Print the results
    print("Generated Random List:", random_list)
    print("Sorted List:", sorted_list)
    print("Sum of the List:", total_sum)
    print("Average of the List:", average)

if __name__ == "__main__":
    main()