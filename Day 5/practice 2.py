# tuple = it is immutable can't modify tuple

x = ()
print(type(x))

y = tuple()
print(type(y))

x = (1, 2, 3)
print(x, type(x))
'''
print(x[0])
x[0]= 5
print(x)
'''
y = (1, 2, 4.5, 'iit', 'kanpur')
print(y)

x = ("patna")
print(x, type(x))
x = ("patna",)
print(x, type(x))

x = (1,2,3,5,1,3,1,5,1,7)
print(x.count(1))
print(x.index(3))