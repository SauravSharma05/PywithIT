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

child_instance = Child()
child_instance.skills()   
child_instance.talents()  
child_instance.hobbies()   

