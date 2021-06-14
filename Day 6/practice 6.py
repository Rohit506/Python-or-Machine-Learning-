# arbitrary argument ** means work in dictionary
def show(**name):
    print(name, type(name))
    for i in name:
        print(i, "\t", name[i], "\t", type(name))
show()
show (a="Ayush", b="Aditi", c="Uttam", d="Anish", e="Lalit")