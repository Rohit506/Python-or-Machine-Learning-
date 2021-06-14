# set operations
x = {1, 2, 3, 8, 9}
y = {4, 5, 6, 7, 8, 9}
# there are two methods to find the union of two sets
print("Union : ", x|y)
print("Union :", x.union(y))

# Find intersection
print("intersection: ",x&y)
print("intersection: ", x.intersection(y))

# Find Difference
print("Difference: ", x-y)
print("Difference: ", x.difference(y))
print("difference: ",y-x)

# symmetric difference
print("Symmetric: ", x^y)
print("Symmetric: ", x.symmetric_difference(y))

x = {1, 2, 3, 8, 9}
y = {4, 5, 6, 7, 8, 9}

a = {1, 2, 3}
print(a.issubset(x))
print(x.issuperset(y))
print(x.issuperset(a))

x = [1, 9, 8, 5, 7, 2, 4, 2]
print (max(x))
print (min(x))
print(sorted(x))
print(len(x))
print(sorted(x, reverse = True))