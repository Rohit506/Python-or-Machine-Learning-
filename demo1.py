
def fun1():
    print("function fun1 of demo1.py")

def add(x,y):
    return x+y

def add2(x):
    if(isinstance(x,list)):
        return sum(x)
    else:
        return "can't add"
'''fun1()
print(add(2,3))
print(add2([1, 2, 3]))
print(add2(2))'''
