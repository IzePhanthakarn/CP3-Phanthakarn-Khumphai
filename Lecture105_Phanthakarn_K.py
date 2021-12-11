class Vehicle:
    lecenseCode = ""
    serialCode = ""
    color = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Pickup(Vehicle):
    pass;

class Normal(Vehicle):
    pass;

class Van(Vehicle):
    pass;

pickupCar = Pickup()
pickupCar.turnOnAirConditioner()
pickupCar.color = "red"
print(pickupCar.color)

normalCar = Normal()
normalCar.turnOnAirConditioner()
normalCar.color = "blue"
print(normalCar.color)

vanCar = Van()
vanCar.turnOnAirConditioner()
vanCar.color = "yellow"
print(vanCar.color)