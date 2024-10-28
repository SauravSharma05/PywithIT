# mutalble classes 
class Pointer:
    def __init__(self, value):
        self.value = value

def increment_pointer(ptr):
    ptr.value += 1  

ptr = Pointer(10)
print("Before increment:", ptr.value)  
increment_pointer(ptr)
print("After increment:", ptr.value)  


class Car:
    def __init__(self, make, model, year):
        self.make = make  
        self.model = model  
        self.year = year 

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)  
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

my_car = Car("Honda", "Civic", 2021)
my_car.display_info()  