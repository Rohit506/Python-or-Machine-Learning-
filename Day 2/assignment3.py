# WAP to find Factorial of a number

import math
num = eval(input("Enter a number for factorial:"))
if( num > 0 ):
    print(math.factorial(num))
else:
    print("Sorry, factorial does not exist for negative numbers")