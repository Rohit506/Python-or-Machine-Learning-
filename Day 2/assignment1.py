# WAP to check a given is odd or even

num = eval(input("Enter a number: "))   # eval() can store int or float both as an input
if(num%2 == 0):
    print(num, "is even number.")
else:
    print(num,"is odd number.")