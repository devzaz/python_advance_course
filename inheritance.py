class Vehicle:
    def general_usage(self):
        print("general use: transportation")


class Car(Vehicle):
    def __init__(self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True


    def specific_usage(self):
        print("specific use: commute to work, vacation with family")



class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm moto cycle")
        self.wheels = 2
        self.has_roof = True

    def specific_usage(self):
        print("specific use: road trip")


c = Car()


m = MotorCycle()


print(issubclass(Car, Vehicle))
print(isinstance(c, Car))
