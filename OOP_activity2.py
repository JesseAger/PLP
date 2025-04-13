class Vehicle:
    def move(self):
        print("This vehicle moves in a general way.")

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

# Test polymorphism
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
