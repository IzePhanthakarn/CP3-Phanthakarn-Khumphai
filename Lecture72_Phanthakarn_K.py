menuList = []
totalPrice = 0
def menu_preview():
    totalPrice = 0
    print("Menu Preview".center(20,"-"))
    for i in range(len(menuList)):
        print(menuList[i][0],"price", menuList[i][1], "B")



while True:
    menu = input("Enter your menu : ")
    if menu.lower() == "exit":
        break
    else:
        price = int(input("Price : "))
        menuList.append([menu, price])
        totalPrice += price

menu_preview()
print("Total price :", totalPrice, "B")