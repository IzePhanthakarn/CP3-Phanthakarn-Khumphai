systemMenu = {"ไก่ทอด": 35, "เป็ดทอด": 45, "ปลาทอด": 55, "ผักทอด": 20}
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
        menuList.append([menu, systemMenu[menu]])
        totalPrice += systemMenu[menu]

menu_preview()
print("Total price :", totalPrice, "B")