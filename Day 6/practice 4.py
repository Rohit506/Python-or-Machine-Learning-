# Function
def show(a, b, c):
    """ It will display all parameter """
    print("a = ",a)
    print("b = ",b)
    print("c = ",c)
show(10, 20, 30)
print("*"*20)
# passing default argument in function
def show(a, b, c = 50):     # passing default value in parameter from left hand side
    """ It will display all parameter """
    print("a = ",a)
    print("b = ",b)
    print("c = ",c)
show(10, 20,)
print("*"*20)
# Default value argument
def show(a =100, b = 30, c = 50):
    """ It will display all parameter """
    print("a = ",a)
    print("b = ",b)
    print("c = ",c)
show()
print("*"*20)
# passing the value in unorderd also
def show(a, b, c):
    """ It will display all parameter """
    print("a = ",a)
    print("b = ",b)
    print("c = ",c)
show(c = 100, a =10, b =50)