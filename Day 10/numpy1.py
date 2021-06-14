import numpy as np

print(np.__version__)
# array - list
a = np.array([5, 10, 15])
print(a)
print("type(a) = ",type(a))

list_a = [1, 2, 3, 4, 5]
print("type(list_a) = ",type(list_a))
b = np.array(list_a)
print(b, type(b))
print(list_a*2)
print(b*2)      # Broadcasting operation
print(b/10)
print("-"*30)

c = np.array([[1, 2], [3, 4], [5, 6]])      # print 2D array
print(c)
d = np.array([1, 2, 3, 4, 5], ndmin=2)      # ndmin for define array dimention
print(d)

e = np.array([3, 4, 5, 6], dtype=float)
print(e)

e = np.array([3, 4, 5, 6], dtype=complex)
print(e)

f = np.asarray([1, 2, 3, 4, 5])
print(f, type(f))
print("-"*30)

def mul(x, y):
    return x*y

x = np.fromfunction(mul, (5, 4))        # here mutiply index(00, 01 ,02....etc) and than print
print(x)
print(np.fromfunction(lambda x,y:x+y+2, (2,2)))
print("-"*30)
print(np.fromfunction(lambda x,y:x+y+2, (5,4)))

a = np.arange(10)
print("a = ",a)
a2 = np.arange(10, 20)
print("a2 = ",a2)
a3 = np.arange(10, 100, 5)
print("a3 = ",a3)

x1 = np.linspace(10, 20, 5, retstep= True)     # 20-10/(5-1)
print(x1)

x2 = np.linspace(10, 20, 5, endpoint= False, retstep= True)
print(x2)

z = np.logspace(1, 2, 10)       # value of log10 =1 to log100 =2, ten values b\w them
print(z)