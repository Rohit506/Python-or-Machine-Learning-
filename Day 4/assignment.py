'''
Write a progamm for
productName = []
productPrice = []
productQuantity = []
press 1: To show all data
Press 2: To add product in cart
press 3: view cart
Press 4: Update (number of cart)
press 5: Delete item from cart
Press 6: Buy item (print invoice)
Press 7: Exit
 '''
print("############# Welcome to mini Shopping mall #############")
print("[1] Press 1: To show all data")
print("[2] Press 2: To add product in cart")
print("[3] press 3: view cart")
print("[4] Press 4: Update.")
print("[5] press 5: Delete item from cart")
print("[6] Press 6: Buy item")
print("[7] Press 7: Exit")
productName = ["Product_Name:", "Pen", "Book", "Mouse", "Keyboard", "CPU", "iPad", "Laptop", "Smartphone", "Chair", "Fan"]
productPrice = ["Price:", 10, 399, 299, 449, 3199, 9999, 21299, 11199, 559, 799]
productQuantity = ["Quantity:", 1000, 600, 200, 500, 100, 90, 50, 150, 300, 700]
mycart = ["Your Product:"]
press = int(input("Press valid key : "))

if(press == 1):
    for i in range(len(productName)):
        print("{:<15}{:<10}{:<10}".format(productName[i], productPrice[i], productQuantity[i]))
elif(press == 2):
    x = input("Enter product name :")
    mycart.append(x)
    print(mycart)
elif(press == 3):
    for a in range(len(mycart)):
        print("{:<15}".format(mycart[a]))
elif(press == 4):
    b = int(input("Enter index number for update: "))
    productName[b] = input("Enter Name of product: ")
    productPrice[b] = input("Enter Price of Quatity: ")
    productQuantity[b] = input("Enter Quantity of product: ")
    for i in range(len(productName)):
        print("{:<15}{:<10}{:<10}".format(productName[i], productPrice[i], productQuantity[i]))
elif(press == 5):
    for i in range(len(productName)):
        print("{:<15}{:<10}{:<10}".format(productName[i], productPrice[i], productQuantity[i]))
    c = int(input("Enter index number for delete: "))
    del productName[c]
    del productPrice[c]
    del productQuantity[c]
    for i in range(len(productName)):
        print("{:<15}{:<10}{:<10}".format(productName[i], productPrice[i], productQuantity[i]))
elif(press == 6):
    print("Buy products")      # work later on this
elif(press == 7):
    print("Thank You")
else:
    print("Entered number is not valid!")