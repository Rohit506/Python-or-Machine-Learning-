# function
x = 10          # Global varaible
def display():
    x = 20      # Local variable
    print("value of x inside display : ",x)
display()
print("value of x outeside display :",x)
print("*"*40)

x = 10
def display():
    global x    # without using global x we can't do operation x = x*2 bcz local
    x = x*2     # Local variable
    print("value of x inside display : ",x)
display()
print("value of x outeside display :",x)