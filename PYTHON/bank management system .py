class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f" {amount} deposited successfully.")
        else:
            print(" Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(" Insufficient balance.")
        elif amount <= 0:
            print(" Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"✅ {amount} withdrawn successfully.")

    def check_balance(self):
        print(f" Current Balance: {self.balance}")

    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")



accounts = {}

while True:
    print("\n====== BANK SYSTEM ======")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display Details")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        acc_no = input("Enter account number: ")
        
        if acc_no in accounts:
            print(" Account already exists!")
        else:
            accounts[acc_no] = BankAccount(name, acc_no)
            print(" Account created successfully!")

    elif choice == "2":
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            amount = float(input("Enter amount to deposit: "))
            accounts[acc_no].deposit(amount)
        else:
            print(" Account not found.")

    elif choice == "3":
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            amount = float(input("Enter amount to withdraw: "))
            accounts[acc_no].withdraw(amount)
        else:
            print(" Account not found.")

    elif choice == "4":
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            accounts[acc_no].check_balance()
        else:
            print(" Account not found.")

    elif choice == "5":
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            accounts[acc_no].display_details()
        else:
            print(" Account not found.")

    elif choice == "6":
        print(" Exiting... Thank you!")
        break

    else:
        print(" Invalid choice. Try again.")