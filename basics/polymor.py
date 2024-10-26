
# polymorphism
print(len("Hello"))               
print(len([1, 2, 3, 4]))          
print(len((1, 2, 3)))              
print(len({"a": 1, "b": 2}))      


class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def move(self):
        return "Driving on the road!"

class Boat(Vehicle):
    def move(self):
        return "Sailing on water!"

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky!"

vehicles = [Car(), Boat(), Plane()]

for vehicle in vehicles:
    print(vehicle.move())