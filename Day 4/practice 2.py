x = "I am a Hacker!"
print(list(x))

# use of split() function
x = "I am a Hacker!"
mylist = x.split(" ")
print(list(mylist), type(mylist), len(mylist))
'''
x= input("Enter the element with space:")
mylist= x.split(" ")
print(mylist)
'''
'''
mylist = input("Enter the element with space :").split(" ")
print(mylist, type(mylist))
'''
# use of append() function
mylist = [3, 2, 1, "iit", "patna"]
print(mylist)
mylist.append("Begusarai")
print(mylist, len(mylist))
mylist.append([1, 2, 3])
print(mylist)
print(len(mylist))

# use of extend() function
mylist.extend([7, 8, 9])
print(mylist)
print(len(mylist))

# use of insert() function
mylist.insert(4, "delhi")
print(mylist)
print(len(mylist))

# How to update list
mylist[2] = 100
print(mylist)
print(len(mylist))
mylist[:3] = 100,200,300
print(mylist)
print(len(mylist))

# how to remove an element
mylist.remove(100)
print(mylist)
print(len(mylist))

# how to reverse the all element
mylist.reverse()
print(mylist)
print(len(mylist))

del mylist[1]           # how to delete element from list
print(mylist, len(mylist))
del mylist[1:3]         # for multiple deletion
print(mylist, len(mylist))