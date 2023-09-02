

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your balance is ${self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount} deposited successfully."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"${amount} withdrawn successfully."
        else:
            return "Insufficient funds."

def main():
    print("Welcome to the Simple ATM Machine")
    atm = ATM()

    while True:
        print("\n Please choose an option:")
        print("Press 1 Check Balance")
        print("Press 2 Deposit")
        print("Press 3 Withdraw")
        print("Press 4 Quit")

        choice = input("Enter your choice : ")

        if choice == "1":
            print(atm.check_balance())
        elif choice == "2":
            amount = float(input("Enter the deposit amount: $"))
            print(atm.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: $"))
            print(atm.withdraw(amount))
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
