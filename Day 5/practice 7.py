# Dictionary comprehension
mydict = {x : x*x for x in range(6)}
print(mydict)

mydict = {x: x*x for x in range(10) if x%2==0}
print(mydict)

mydict = {x: x*x for x in range(10,0,-1) if x%2==0}
print(mydict)

'''
// :- floor division
** :- power
in c :- &&, ||, !
Python:- and, or, not
'''
print(5/2)
print(5//2)     #floor division provide low result in int
print(10/3)
print(10//3)