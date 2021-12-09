def vatCalculate(price):
    totalPrice = price + (price*7)/100
    return totalPrice

price = int(input("Enter your price : "))
print("Your total price = ",vatCalculate(price), "B")