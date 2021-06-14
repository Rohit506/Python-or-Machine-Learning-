# arbitrary argument : using this argument method we can pass nth number of value
# In this type of argument we store data in tuples only
def show(*name) :
    for x in name :
        print(x, type(name), x.upper())
show ('Rohit', 'Stuti', 'Monu')
print("*"*30)
show ("Ayush", "Aditi", "Uttam", "Anish", "Lalit")