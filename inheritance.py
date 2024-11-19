class Device:
    def __init__(self, height, width, name):
        self.height = height
        self.width = width
        self.name = name

    def power_on():
        print("The device powered on")

class Computer(Device):
    def power_on():
        print("The computer powered on")

    def add(self, num1, num2):
        print(f"{num1} + {num2} = {num1 + num2}")

    def multiply(self, num1, num2):
        print(f"{num1} * {num2} = {num1 * num2}")


class Vehicle:
    def __init__(self, name, speed, size):
        self.name = name
        self.speed = speed
        self.size = size

    def switch_on(self):
        print("The vehicle turned on")

    def drive(self):
        print("The vehicle is being driven")

    def fix(self):
        print("The vehicle has been fixed")

class Car(Vehicle):
    def switch_on(self):
        print("The car turned on")

    def drive(self):
        print("The car is being driven")

    def fix(self):
        print("The car has been fixed")

    def vehicle_compare(self, vehicle: Vehicle):
        if self.speed > vehicle.speed:
            print(f"{self.name} is faster than {vehicle.name}")
        else:
            print(f"{self.name} is slower than {vehicle.name}")

class Motorbike(Vehicle):
    def switch_on(self):
        print("The motorbike turned on")

    def drive(self):
        print("The motorbike is being driven")

    def fix(self):
        print("The motorbike has been fixed")

    def crash(self):
        print("The motorbike has crashed")


device = Device(10, 20, "Laptop")
computer = Computer(30, 50, "Computer")

vehicle = Vehicle("Truck", 10, 40)
car = Car("Car", 50, 20)
motorbike = Motorbike("Motorbike", 30, 5)