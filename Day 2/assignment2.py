# WAP to create a user menu
# Press 1 for addition
# Press 2 for subtraction
# Press 3 for multiplication
# Press 4 for division

print("Press 1 for Addition.")
print("Press 2 for Subration.")
print("Press 3 for Multiplication.")
print("Press 4 for Division.")

n = eval(input("Press valid number for operation : "))

if (n == 1):
    num1 = eval(input("Enter 1st number: "))
    num2 = eval(input("Enter 2nd number: "))
    result = num1 + num2;
    print("Result sum = ", result)
elif(n == 2):
    num1 = eval(input("Enter 1st number: "))
    num2 = eval(input("Enter 2nd number: "))
    result = num1 - num2;
    print("Result subtraction = ", result)
elif(n == 3):
    num1 = eval(input("Enter 1st number: "))
    num2 = eval(input("Enter 2nd number: "))
    result = num1*num2;
    print("Result multiply = ", result)
elif(n == 4):
    num1 = eval(input("Enter 1st number: "))
    num2 = eval(input("Enter 2nd number: "))
    result = num1/num2;
    print("Result division = ", result)
else:
    print("Please press valid number")