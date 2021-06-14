
def show():
    print("show function.")

def display():
    print("It will return the address of show")
    return show         # it returns addres of show function
x = display()           # address of show function stored in x
print("-"*30)
x()                     # now call the show function using their address