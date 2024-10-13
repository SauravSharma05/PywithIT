# class car:
#    car1 = 'mercedes'
#    car2 = 'bmw'

# name1 = car()
# print(name1.car2, name1.car1)

# name2 = car()
# print(name2.car1)               // similarly we can make another object with same 


# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         print(f"{self.name} say hi!")

# my_dog = Dog("hello", "german shephard")
# my_dog.bark()

class Car:
    type_of_vehicle = "Automobile"

    def __init__(self, model, year):
        self.model = model  
        self.year = year    

    def honk(self):
        return "Beep!"

my_car = Car("Toyota", 2020)

print(my_car.model)       
print(my_car.year)        
print(my_car.honk())     


