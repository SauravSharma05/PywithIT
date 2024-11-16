from collections import Counter

list1 = [1, 2, 3, 3]
list2 = [3, 2, 1]

# Compare using Counter
print(Counter(list1) == Counter(list2))  



list1 = [1, 2, 3]
list2 = [2, 3, 4]

diff = [x for x in list1 if x not in list2]
print(diff) 

list1 = [5, 3, 1]
list2 = [1, 5, 3]

# Sort and compare
print(sorted(list1) == sorted(list2))  



#map and reduce

from functools import reduce

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 30, 40, 50]
list3 = [10, 20, 30, 40, 60]

def compare_lists(l1, l2):
    comparison_results = map(lambda x, y: x == y, l1, l2)
    return reduce(lambda x, y: x and y, comparison_results)

print("List1 and List2 are equal:", compare_lists(list1, list2))  
print("List1 and List3 are equal:", compare_lists(list1, list3))  


# object handling 

class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def display_info(self):
        return f"Model: {self.model}, Price: {self.price}"

print(my_car.display_info())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

person1 = Person("Alice", 30)
print(person1)  

print(getattr(person1, 'name'))
setattr(person1, 'age', 31)
print(person1)  