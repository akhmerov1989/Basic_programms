# Fibonacci seq - series of numbers is the sum of the two preceding ones.
# 0,1,1,2,3,5,8,13,21,34,55,89,144 ...
nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

# check if hte number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
# generate fibonacci sequence
else:
    print("Fibonacci swquence: ")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1


# Fibonacci sequence using recursion

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


nterms_2 = int(input("Enter the number of terms (greater than 0): "))

# Check if the number of terms is valid
if nterms_2 <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence: ")
    for i in range(nterms_2):
        print(recur_fibo(i))
