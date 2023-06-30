
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: Division by Zero")
        return None

def calculator():
    print("WELCOME TO JUDITH COMMAND LINE CALCULATOR")
    print("Available Operation")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        choice = input("ENTER THE OPERATION NUMBER (1 - 4)")

        if choice == "0":
            print("Exiting the Calculator")
            break

        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter the first number"))
            num2 = float(input("Enter the second number"))

            if choice == "1":
                result = add(num1, num2)
                print("Result: ", result)
            elif choice == "2":
                result = subtract(num1, num2)
                print("Result: ", result)
            elif choice == "3":
                result = multiply(num1, num2)
                print("Result: ", result)
            elif choice == "4":
                result = divide(num1, num2)
                if result is not None:
                    print("Result: ", result)
        else:
            print("Invalid choice please enter a number from (1 - 4)")

calculator()













