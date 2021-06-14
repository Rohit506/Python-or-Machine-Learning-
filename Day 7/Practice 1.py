# creating function inside function
def outerfunction():
    x = 100
    y = 500
    def innerfunction():
        x = 10
        y = 20
        print("inside inner function x:",x)
        print("inside iner function y:",y)
    innerfunction()
    print("inside outer funcion x :",x)
    print("inside outer function y :",y)
outerfunction()
print("-"*50)               # Line seperator

def outerfunction():
    x = 100
    y = 500
    def innerfunction():
        nonlocal x      # nonlocal x means it change the value of outerfunction's x value to innerfunction's x = 10
        x = 10
        y = 20
        print("inside inner function x:",x)
        print("inside iner function y:",y)
    innerfunction()
    print("inside outer funcion x :",x)
    print("inside outer function y :",y)
outerfunction()
