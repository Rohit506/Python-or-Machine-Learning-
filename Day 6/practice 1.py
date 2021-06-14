# Function : A group of statement that perform certain task, function helps to break program in small chunk
# syntax of function
'''
def function name(parameter) :
    [""" Doc string """]            -------> optional
    Statement 1
    statement 2
    statement 3
    -------
    [return]               -------> optional
'''

def say(name):
    """ It is my first function
    it can display a message
    Good Morning with name"""
    print("good Morning", name)
say("Rohit")
print("Documentation :", say.__doc__)      #it will print the documentation of function
res = say("Anish")
print(res)              #if don't return any value in function then call the "res" it will print "None"