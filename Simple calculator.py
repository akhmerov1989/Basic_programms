# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers

def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    # Check if choice is one of four options
    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))
        elif choice == '2':
            print(num1, "-",num2, "=", subtract(num1,num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1,num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1,num2))

        # Check if user wants another calculation
        # Break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == 'yes':
            continue
        elif next_calculation == 'no':
            break
        else:
            print("Invalid. Try again")

    else:
        print("Invalid input")
