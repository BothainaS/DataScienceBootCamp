class ATM:
  #initiaize the attribute whith defalt balance amount 5000
    def __init__(self, balance=5000):
        self.balance = balance

    def check_balance(self):
        return f"Your account balance is SR{self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            return f"SR{amount} has been deposited into your account."
        else:
            return "Invalid amount. Please deposit a positive amount."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance = self.balance - amount
                return f"SR{amount} has been withdrawn from your account."
            else:
                return "Insufficient funds. Please choose a smaller amount."
        else:
            return "Invalid amount. Please withdraw a positive amount."


def main():
    atm = ATM()
    while True:
        print("Options:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(atm.check_balance())
        elif choice == "2":
            amount = float(input("Enter the deposit amount: "))
            print(atm.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: "))
            print(atm.withdraw(amount))
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
