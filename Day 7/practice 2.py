# reduce function:
# reduce takes two argument function or list
mylist = [1, 2, 3, 4, 5, 6]
import functools
x = functools.reduce(lambda x,y: x+y, mylist)
print(x)

# how to do function renaming
def fun():
    print("Fun function.")
a = fun
a()