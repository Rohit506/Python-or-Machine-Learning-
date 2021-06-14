# Strings

x = 'iit kAnpur'
print(x.upper())
print(x.lower())
print(x.index('n'))
print(x.count('i'))
print(x.split(" "))
print(x.title())
print(x.capitalize())
print(x.swapcase())
print(x.isidentifier())
y = "abc_"
print(y.isidentifier())
print(y.isalpha())
print(y.isalnum())
print(x.replace('i', 'e'))

frnds = {"Rohit", "Uttam", "Anish", "Adity", "Aman", "Amit", "Raushan", "Kapil", "Deepa"}
for i in frnds:
    if(i.startswith('A')) :
        print(i, end = "  ")
print()
list_files = ["a.mp3", "b.pdf", "c.mp3", "d.docx", "e.pdf"]
for x in list_files:
    if(x.endswith('.pdf')):
        print(x, end = "  ")