# import custom module which is created by myself "demo1.py"
import demo1
demo1.fun1()
print(demo1.add(10, 20))
print(demo1.add2([1, 2, 3, 4, 5, 6]))
print("-"*50)

# giving "alias" name or you can say nikname
import demo1 as d
d.fun1()
print(d.add(100, 200))
print(d.add2([100, 200, 300, 400]))
print("-"*50)

# import only two function fun1 or add from module demo1
from demo1 import fun1,add
fun1()
print(add(30,15))
print("-"*50)

# if i want to import all function then use "*"
from demo1 import*
print(add(7,78))
print(add2([7,4,9,4,9]))
