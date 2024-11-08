# Private attribute
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance is {self.__balance}."
        return "Deposit amount must be positive."

    def get_balance(self):
        return self.__balance

account = BankAccount("Alice")
print(account.deposit(100))       
print(account.get_balance())      