# Traditional System
mylist = []
for i in range(10) :
    mylist.append(2**i)   # double multiplication(**) denotes as a power of number
print(mylist)

# List Comprehension
mylist2 = [3**x for x in range(10)]
print(mylist2)
list = [3**x for x in range(10) if x%2==1]
print(list)