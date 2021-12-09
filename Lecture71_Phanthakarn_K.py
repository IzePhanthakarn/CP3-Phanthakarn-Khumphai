menuList = []
priceList = []


def menu_preview():
    totalPrice = 0
    print("----Menu Preview----")
    for i in range(len(menuList)):
        print(menuList[i],"price", priceList[i], "B")
        totalPrice += int(priceList[i])
    print("Total =", totalPrice, "B")


while True:
    menu = input("Enter your menu : ")
    if menu.lower() == "exit":
        break
    else:
        price = int(input("Price : "))
        menuList.append(menu)
        priceList.append(price)
menu_preview()