# simple interest calculate 
def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time in years: "))

    simple_interest = calculate_simple_interest(principal, rate, time)

    print(f"The simple interest is: {simple_interest:.2f}")

# executing function
if __name__ == "__main__":
    main()