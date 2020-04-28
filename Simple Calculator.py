import sys
while True:
    print("Welcome To My Simple Calculator")
    print("Enter this Abbreviations To Continue")
    print("Enter + for Adding")
    print("Enter - for Substractiing")
    print("Enter * for Multiplication")
    print("Enter / for Dividing")
    print("Enter ** for Exponation")
    print("To quit Enter Q")
    user_input = input(":")
    if user_input == "Q":
        sys.exit()
    elif user_input == "+":
        print("You have Enter Adding")
        num1 = (float(input("You have to Enter a number")))
        num2 = (float(input("Enter another number")))
        result = (str(num1 + num2))
        print(result)

    elif user_input == "-":
        print("You have Enter Substraction")
        num1 = (float(input("You have to Enter a number")))
        num2 = (float(input("Enter another number")))
        result = (str(num1 - num2))
        print(result)
    elif user_input == "*":
        print("You have Enter Adding")
        num1 = (float(input("Enter a number")))
        num2 = (float(input("Enter a number")))
        result = (str(num1 * num2))
        print(result)
    elif user_input == "/":
        print("You have Enter Adding")
        num1 = (float(input("Enter a number")))
        num2 = (float(input("Enter a number")))
        result = (str(num1 / num2))
        print(result)
    elif user_input == "**":
        print("You have Enter Adding")
        num1 = (float(input("Enter a number")))
        num2 = (float(input("Enter a number")))
        result = (str(num1 ** num2))
        print(result)
    else:
        sys.exit()
        print("You have enter the wrong choice Goodbye")
