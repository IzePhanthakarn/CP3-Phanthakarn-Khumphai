usernameInput = input("Username :")
passwordInput = input("Password :")

if usernameInput  == "admin"  and passwordInput == "1234":
    print("Done !")
    print("----- Welcom to fruit shop -----")
    print(" 1. Orange : 15 B")
    print(" 2. Mango : 20 B")
    print(" 3. Rose apple : 10 B")
    print(" 4. Watermelon : 40 B")
    userSelect = int(input("Please select fruit : "))
    if (userSelect == 1):
        userQuantity = int(input("How many do you want?\nI want : "))
        price = userQuantity * 15
    elif (userSelect == 2):
        userQuantity = int(input("How many do you want?\nI want : "))
        price = userQuantity * 20
    elif (userSelect == 3):
        userQuantity = int(input("How many do you want?\nI want : "))
        price = userQuantity * 10
    elif (userSelect == 4):
        userQuantity = int(input("How many do you want?\nI want : "))
        price = userQuantity * 40
    else:
        print("error")
    print("Total", price, "B")
else:
    print("error")