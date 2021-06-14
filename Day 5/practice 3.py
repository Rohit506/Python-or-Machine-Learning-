# sets in python
x = set()
print(x, type(x))

x = {1, 2, 3}
print(x, type(x))

x = {1, 2, 3, 1, 2, 3, 4, 5, 6,1}
print(x)
# There is no concept of indexing
# we can add or remove the item from set using add() or remove()
x.add('a')
print(x)
x.remove(1)
print(x)
'''
Difference b/w remove() and discard() is that , if we use remove() and try to remove element
which is present in set it gives error
when we use discard() and try to remove item ffrom set which is not present in set it gives not error
'''
x = set("helloworld")
print(x)
x.discard('e')
print(x)