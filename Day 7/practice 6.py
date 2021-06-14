# math package
import math
print("Factorial of 5: ",math.factorial(5))
print("Sum of List: ",math.fsum([1, 3,5, 7,4, 7,5]))    # it gives the output in float

print("List of math package methods: ",dir(math))
print("floor function of 3.5 : ",math.floor(3.5))       # floor provide us lower number
print("floor function of -3.5 : ",math.floor(-3.5))

print("ceil value of 3.5: ",math.ceil(3.5))             # floor provide us lower number
print("ceil value of -3.5: ",math.ceil(-3.5))
print("Absolute value of -3.4: ",math.fabs(-3.4))       # it give moduloa of number

print("Radian of 90: ",math.radians(90))
print("Radian of 45: ",math.radians(45))

print("sin 90: ",math.sin(math.radians(90)))        # radian is necessary for getting correct output
print("cos 90: ",math.cos(math.radians(90)))
print("-"*100)

# find sin value of all which is present in list
list1 = [0, 30, 45, 60, 90]
newlist = list(map(lambda i: math.sin(math.radians(i)),list1))
print("Sin value in newlist: ", newlist)
print("-"*100)

print("PI value: ",math.pi)
print("e value: ", math.e)
print("-"*100)

print("Log 10: ",math.log10(11))

# print log value of every number
mylist1 = range(1, 101)         # log10 (0) is not value in math so get error
x = list(mylist1)
newlist1 = list(map(lambda x: math.log10(x), x))
print(newlist1)