#basic compund interest calc

def calculate_compound_interest(principal, rate, times_compounded, years):
    rate_decimal = rate / 100
    total_amount = principal * (1 + rate_decimal / times_compounded) ** (times_compounded * years)
    return total_amount

def main():
    print("Welcome to the Compound Interest Calculator!")

    principal = float(input("Enter the principal amount : "))
    rate = float(input("Enter annual interest rate : "))
    times_compounded = int(input("Enter number of times that interest is compounded: "))
    years = float(input("Enter years : "))

    total_amount = calculate_compound_interest(principal, rate, times_compounded, years)

    print(f"\nTotal amount after {years} years: ${total_amount:.2f}")

if __name__ == "__main__":
    main()


    class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        return "Some sound"

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__("Cat")
        self.name = name
        self.age = age

    def make_sound(self):
        return f"{self.name} says Meow!"

my_cat = Cat("Whiskers", 2)
print(my_cat.make_sound())