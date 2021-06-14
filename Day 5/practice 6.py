
mydict = {1001: "Rohit", 1002: "Anish", 1003: "Uttam", 1004: "Nikhil", 1005: "Prabhat"}
for i in mydict:
    print(i, "\t", mydict[i])

mydict.pop(1001)
print(mydict)
print(mydict.values())
print(mydict.items())
print(mydict.keys())
# update
x = mydict[1002]
del mydict[1002]
mydict[1008] = x
print(mydict)