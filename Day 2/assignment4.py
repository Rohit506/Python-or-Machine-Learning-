

n = eval(input("Enter terms:"))
Number = 1

while (Number <= n):
    count = 0
    i = 2

    while (i <= Number // 2):
        if (Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" % Number, end='  ')
    Number = Number + 1