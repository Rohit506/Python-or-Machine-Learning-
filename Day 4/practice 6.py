# what is immutable or mutable
'''
x = 'kanpur'        # string is immutable can't change or update after declaration
x[1] = 'm'
print(x)
'''
x = 'iit'
y = ' kanpur'
z = x+y     # concatenate the string
print(z)
print(y*3)  # here * mean repetation

# format{} function
sentence = "Name ={} Age ={} Mark ={}".format('Rohit',21,421)
print(sentence)
sentence2 = "First Name :{1}, Middle Name :{0}, Last Name :{2}".format('sharma', 'Kumar', 'Rohit')
print(sentence2)
sentence2 = "First Name :{a}, Middle Name :{b}, Last Name :{c}".format(c='sharma', b='Kumar', a='Rohit')
print(sentence2)