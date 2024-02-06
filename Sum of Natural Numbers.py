# NN - are a set of positive integers that are used to count and order objects
# N - 1,2,3,4,5,6,7,8...

limit = int(input("Enter the limit: "))

# Initialize the sum
sum_nn = 0

# Use a for loop to calculate the sum of natural numbers
for i in range(1, limit + 1):
    sum_nn += i
#  Print the sum
print("The sum of natural numbers up to", limit, "is:", sum_nn)