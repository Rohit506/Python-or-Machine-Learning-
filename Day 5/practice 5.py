
mydict = {}
print(mydict, type(mydict))

mydict2 = dict()
print(mydict2, type(mydict2))

mydict = {1001: "Rohit", 1002: "Anish", 1003: "Uttam", 1004: "Nikhil", 1005: "Prabhat"}
print(mydict, type(mydict))

mydict3 = {'name': 'rohit', 1: [1, 2, 3], 2: (10, 20)}
print(mydict3, type(mydict3))
print(mydict[1003])
print(mydict3[2])
# keyerror  print(mydict[1006])
# update
mydict[1005] = "Munna"
print(mydict)
# delete
del mydict[1005]
print(mydict)