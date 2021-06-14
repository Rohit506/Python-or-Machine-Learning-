# Filter or Map function

# Filter function takes two argument one is function and second is list
# this function is called with all item in the list and a new list is return
# which contains item for which the function evaluates true
# it print particular element from List in new list
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

newlist = list(filter(lambda x: x%2 == 0, mylist))
print("New List of Filter function: ", newlist)

newlist = list(filter(lambda x: x>=8 and x<=12, mylist))
print("New List of Filter function: ", newlist)
print("*"*100)

# Map it also takes two argument function and list
# Map prints all element in new list
newlist2 = list(map(lambda x: x*2, mylist))
print("new list using map function :",newlist2)

newlist2 = list(map(lambda x: x*x, mylist))
print("new list using map function :",newlist2)

newlist2 = list(map(lambda x: x>6, mylist))
print("new list using map function :",newlist2)
