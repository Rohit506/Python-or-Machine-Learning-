

name = ['Rohit', 'Anish', 'Uttam']
city = ['Begusarai', 'Jamui', 'Patna']
branch = ['CSE', 'IT', 'ECE']
for i in range(len(name)):
    print("{:<15}{:<15}{:<5}".format(name[i], city[i], branch[i]))      # here use this {:<15},{:>10},{:^5} Left, Right or Center allignment spaces

# Row String
print(r"iit kanpur\n patna")
name = r"iit patna\n kanpur\t Delhi there is\x61 training\n of good student."
print(name)

# unicode in hexadecimal
x = u'\u0905\u092D\u093F'    # search unicode on google
print(x)