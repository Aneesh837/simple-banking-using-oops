class BankingProgram:
    def __init__(self):
        self.balance = 0

    def show_balance(self):
        print(f"Your balance is ${self.balance:.2f}")

    def deposit(self):
        amount = float(input("Enter an amount to be deposited: "))

        if amount < 0:
            print("That's not a valid amount")
            return 0
        else:
            return amount

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))

        if amount > self.balance:
            print("Insufficient funds")
            return 0
        elif amount <= 0:
            print("Amount must be greater than 0")
            return 0
        else:
            return amount

    def run(self):
        is_running = True
        while is_running:
            print("*********************")
            print("   Banking Program   ")
            print("*********************")
            print("1.Show Balance")
            print("2.Deposit")
            print("3.Withdraw")
            print("4.Exit")
            print("*********************")
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.show_balance()
            elif choice == '2':
                self.balance += self.deposit()
            elif choice == '3':
                self.balance -= self.withdraw()
            elif choice == '4':
                is_running = False
            else:
                print("That is not a valid choice")

        print("*********************")
        print("Thank you! Have a nice day!")
        print("*********************")
if __name__ == "__main__":
    program = BankingProgram()
    program.run()
