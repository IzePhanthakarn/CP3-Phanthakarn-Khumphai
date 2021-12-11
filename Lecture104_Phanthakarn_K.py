class Customer:
    firstName = ""
    lastName = ""
    age = 0
    def addCart(self):
        print("Added product to",self.firstName,self.lastName,"'s cart")

customer1 = Customer()
customer1.firstName = "Phanthakarn"
customer1.lastName = "K"
customer1.addCart()

customer2 = Customer()
customer2.firstName = "Waraphorn"
customer2.lastName = "J"
customer2.addCart()

customer3 = Customer()
customer3.firstName = "Pichanat"
customer3.lastName = "K"
customer3.addCart()

customer4 = Customer()
customer4.firstName = "Somphong"
customer4.lastName = "L"
customer4.addCart()

customer5 = Customer()
customer5.firstName = "Warisara"
customer5.lastName = "S"
customer5.addCart()