name = 'iit kanpur'
print(name[4:])
print(name[-3:])
print("Empty", name[-1:-3])      # output null or empty because try to print in reverse
print(name[::-1])

# WAP to check Palindrome or not
x = input("Enter word or number to check palidrome :")
if x == x[::-1]:
    print("It is palindrome.")
else:
    print("It is not palindrome.")