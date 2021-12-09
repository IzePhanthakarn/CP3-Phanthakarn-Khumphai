def login():
    print("Login form")
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    while usernameInput != "admin" or passwordInput != "1234":
        print("username or password was wrong !")
        usernameInput = input("Username : ")
        passwordInput = input("Password : ")
    print("Login success")
    showMenu()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">> "))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

login()
userSelected = menuSelect()
if (userSelected == 1):
    print(vatCalculator(int(input("Enter your price : "))))
elif (userSelected == 2):
    print(priceCalculator())
