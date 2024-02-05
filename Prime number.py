# Prime number is a whole number that cannot be evenly divided by any other number except for 1 and itself
num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 1:
    print(f"{num}, is mot a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            flag = True  # if factor is found, set flag to True
            # break out of Loop
            break
    # check if flag is True
if flag:
    print(f"{num}, is not a prime number")
else:
    print(f"{num}, is a prime nunber")


def is_prime(number):
    if number <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # Found a divisor, not a prime
    return True  # No divisors found, it's a prime number


# Example usage
num_check = int(input("Enter a number: "))
if is_prime(num_check):
    print(f"{num_check} is a prime number.")
else:
    print(f"{num_check} is not a prime number.")
