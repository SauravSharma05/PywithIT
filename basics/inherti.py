#single inheritance
class Parent:
    def display(self):
        print("parent class.")

class Child(Parent):
    def show(self):
        print("child class.")

child_instance = Child()
child_instance.display()  
child_instance.show()     

#multiple inheritance
class Father:
    def skills(self):
        print("Father's skills")

class Mother:
    def talents(self):
        print("Mother's talents")

class Child(Father, Mother):
    def hobbies(self):
        print("Child's hobbies")

# multilevel
child_instance = Child()
child_instance.skills()   
child_instance.talents()  
child_instance.hobbies()   

class Grandparent:
    def heritage(self):
        print("Grandparent's heritage")

class Parent(Grandparent):
    def profession(self):
        print("Parent's profession")

class Child(Parent):
    def future(self):
        print("Child's future plans")

child_instance = Child()
child_instance.heritage()   
child_instance.profession()  
child_instance.future()      


# heirarchical
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

dog_instance = Dog()
cat_instance = Cat()
dog_instance.sound()  
dog_instance.bark()   

cat_instance.sound()  
cat_instance.meow()   