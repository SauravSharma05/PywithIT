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

# class Car:
#     type_of_vehicle = "Automobile"

#     def __init__(self, model, year):
#         self.model = model  
#         self.year = year    

#     def honk(self):
#         return "Beep!"

# my_car = Car("Toyota", 2020)

# print(my_car.model)       
# print(my_car.year)        
# print(my_car.honk())     



# class Animal: # Constructor to initialize species and habitat
#       def __init__(self, species_name, habitat):
#             self.species_name = species_name
#             self.habitat = habitat
#       
#       def display_info(self):
#       print("Species Name:", self.species_name)
#       print("Habitat:", self.habitat)# Creating instances of Animal with different attributes

# lion = Animal("Lion", "Savannah")
# penguin = Animal("Penguin", "Antarctica")     

# lion.display_info() 
# penguin.display_info() 

# Accessing attributes directly
# print("Species for Lion is", lion.species_name)
# print("Habitat for Penguin is", penguin.habitat)


class Book:
      def __init__(self, title, author):
self.title = title
self.author = author
booktitle1 = input("Enter the title of the first book: ")
author1 = input("Enter the author of the first book: ")
book1 = Book(title1, author1)

booktitle2 = input("Enter the title of the second book: ")
author2 = input("Enter the author of the second book: ")
book2 = Book(title2, author2)

print("\nBook 1:")
print(f"Title: {book1.title}, Author: {book1.author}")
print("\nBook 2:")print(f"Title: {book2.title}, Author: {book2.author}")














