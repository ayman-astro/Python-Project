from random import randint
from datetime import datetime


class Bank:
    def __init__(self):
        self.name = "Goriber Bank"
        self.users = []
        self.total_balance = 100000
        self.total_loan = 0
        self.loan = True
        self.bankrupt = False

    def create_account(self, user):
        if user.account_type == "Savings":
            acc_type = "s"
        else:
            acc_type = "c"
        user.account_no = f"gorib-{acc_type}-{randint(10,99)}-{len(self.users)+1}"
        self.users.append(user)
        print(f"\nCongratulation, {user.name}! Account: {user.account_no} is created.")
        print("Plase save your account number.\n")

    def delete_account(self, user_account_no):
        for user in self.users:
            if user.account_no == user_account_no:
                print(f"\nAccount: {user_account_no} is deleted.\n")
                self.total_balance -= user.balance
                self.users.remove(user)
                return
        print(f"\nAccount: {user_account_no} is not found.\n")

    def deposit(self, user, amount):
        if amount > 1:
            user.balance += amount
            self.total_balance += amount
            transaction = {
                "Type": "Deposit",
                "Amount": amount,
                "time": datetime.now(),
            }
            user.transaction_history.append(transaction)
            print(
                f"\n{amount} Taka is credited in your account. Time: {datetime.now()}.\n"
            )
        else:
            print(f"\nAmount can not be less than 1 Taka.\n")

    def withdraw(self, user, amount):
        if self.bankrupt:
            print("\nThe bank is bankrupt.\n")
            return
        if amount <= user.balance:
            user.balance -= amount
            self.total_balance -= amount
            transaction = {
                "Type": "Withdraw",
                "Amount": amount,
                "time": datetime.now(),
            }
            user.transaction_history.append(transaction)
            print(
                f"\n{amount} Taka is debited in your account. Time: {datetime.now()}.\n"
            )
        else:
            print(f"\nWithdrawal amount exceeded.\n")

    def check_balance(self, user):
        print(f"\nYour Balance is: {user.balance} Taka.\n")

    def check_transaction_history(self, user):
        print(f"\nTransaction History of {user.account_no}\n")
        for transaction in user.transaction_history:
            for key, value in transaction.items():
                print(f"{key}: {value}", end="\t")
            print()
        print()

    def take_loan(self, user, amount):
        if self.loan:
            if amount <= self.total_balance:
                if user.loan_taken < 2:
                    user.balance += amount
                    self.total_loan += amount
                    user.loan_taken += 1
                    transaction = {
                        "Type": "Loan",
                        "Amount": amount,
                        "time": datetime.now(),
                    }
                    user.transaction_history.append(transaction)
                    print(
                        f"\nLoan: {amount} Taka is credited in your account. Time: {datetime.now()}.\n"
                    )
                else:
                    print(f"\nSorry! You can not take more than 2 loans.\n")
            else:
                print(f"\nYou can not take {amount} Taka loan.\n")
        else:
            print("\nSorry! Currently loan feature is off.\n")

    def transfer_amount(self, sender, receiver_account_no, amount):
        if amount <= 1:
            print(f"\nTransfer {amount} Taka must be greater than 0.\n")
            return
        for user in self.users:
            if user.account_no == receiver_account_no:
                receiver = user
                if sender.balance >= amount:
                    sender.balance -= amount
                    receiver.balance += amount
                    print(
                        f"\nLoan: {amount} Taka is transfered from {sender.account_no} to {receiver.account_no}. Time: {datetime.now()}.\n"
                    )
                    transaction = {
                        "Type": "Transfer",
                        "Sender Name": sender.name,
                        "Sender Account": sender.account_no,
                        "Receiver Name": receiver.name,
                        "Receiver Account": receiver.account_no,
                        "Amount": amount,
                        "time": datetime.now(),
                    }
                    sender.transaction_history.append(transaction)
                    receiver.transaction_history.append(transaction)
                else:
                    print("\nInsufficient balance for transfer.\n")
                return
        print(f"\nAccount does not exist !!\n")

    def total_bank_balance(self):
        print(f"\nTotal bank balance is: {self.total_balance}.\n")

    def loan_feature(self):
        if self.loan:
            self.loan = False
            print("\nLoan feature is turned off.\n")
        else:
            self.loan = True
            print("\nLoan feature is turned on.\n")

    def declare_bankrupt(self):
        self.bankrupt = True
        print("\nDeclared Bankrupt\n")

    def loan_balance(self):
        print(f"\nTotal bank balance is: {self.total_loan}.\n")

    def view_all_accounts(self):
        print(f"\nAll Account's Informations")
        print("---------------------------")
        i = 1
        for user in self.users:
            print(
                f"{i}.Name: {user.name}\tEmail: {user.email}\tAddress: {user.address}\tAccount Type: {user.account_type}\tAccount: {user.account_no}\tBalance: {user.balance}"
            )
            i += 1
        print()


class Admin:
    def __init__(self):
        self.name = "Admin"
        self.password = "admin123"

    def create_account(self, user, bank):
        bank.create_account(user)

    def delete_account(self, user_account_no, bank):
        bank.delete_account(user_account_no)

    def view_all_accounts(self, bank):
        bank.view_all_accounts()

    def total_bank_balance(self, bank):
        bank.total_bank_balance()

    def total_loan_amount(self, bank):
        bank.loan_balance()

    def loan_feature(self, bank):
        bank.loan_feature()

    def declare_bankrupt(self, bank):
        bank.declare_bankrupt()


class User:

    def __init__(self, name, password, email, address, account_type):
        self.name = name
        self.password = password
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan_taken = 0
        self.transaction_history = []

    def create_account(self, user, bank):
        bank.create_account(user)

    def deposit(self, amount, bank):
        bank.deposit(self, amount)

    def withdraw(self, amount, bank):
        bank.withdraw(self, amount)

    def check_balance(self, bank):
        bank.check_balance(self)

    def check_transaction_history(self, bank):
        bank.check_transaction_history(self)

    def take_loan(self, amount, bank):
        bank.take_loan(self, amount)

    def transfer_amount(self, receiver, amount, bank):
        bank.transfer_amount(self, receiver, amount)


bank = Bank()
admin = Admin()


def admin_menu():
    while True:
        password = input("\nEnter Your Password: ")  # password = admin123
        if password == admin.password:
            print("\nWelcome Admin\n")

            while True:

                print("1. Create New Account")
                print("2. Delete Account")
                print("3. View All Accounts")
                print("4. Total Bank Balance")
                print("5. Total Loan Amount")
                print("6. loan Feature")
                print("7. Declare Bankrupt")
                print("8. Exit")

                try:
                    option = int(input("\nEnter Your Option: "))
                except:
                    print("\nInvalid input !! Please enter a number.\n")
                    continue

                if option == 1:
                    name = input("Enter Your Name: ")
                    email = input("Enter Your Email: ")
                    password = input("Enter Your Password: ")
                    Address = input("Enter Your Address: ")
                    try:
                        account_type = int(
                            input("Enter Your Account Type\n1. Savings / 2. Current: ")
                        )
                    except:
                        print("\nInvalid input! Please enter a number.\n")
                        continue
                    if account_type == 1:
                        account_type = "Savings"
                    else:
                        account_type = "Current"

                    user = User(name, password, email, Address, account_type)
                    admin.create_account(user, bank)

                elif option == 2:
                    account_no = input("Enter Account No: ")
                    admin.delete_account(account_no, bank)

                elif option == 3:
                    admin.view_all_accounts(bank)

                elif option == 4:
                    admin.total_bank_balance(bank)

                elif option == 5:
                    admin.total_loan_amount(bank)

                elif option == 6:
                    admin.loan_feature(bank)

                elif option == 7:
                    admin.declare_bankrupt(bank)

                elif option == 8:
                    return

                else:
                    print("\nInvalid !!")

        else:
            print("\nWrong Password !!\n")
            break


def user_menu():
    while True:

        print("\n1. Login")
        print("2. Create New Account")
        print("3. Exit")

        try:
            option = int(input("\nEnter Your Option: "))
        except:
            print("\nInvalid input! Please enter a number.\n")
            continue

        if option == 1:
            account_no = input("\nEnter Your Account No: ")
            password = input("Enter Your Password: ")

            for user in bank.users:
                if user.account_no == account_no:
                    if user.password == password:
                        print(f"\nWelcome to The Gorib Bank {user.name}\n")

                        while True:
                            print("1. Deposit")
                            print("2. Withdraw")
                            print("3. Check Balance")
                            print("4. Take Loan")
                            print("5. Transfer Amount")
                            print("6. Check Transaction History")
                            print("7. Logout")

                            option = int(input("\nEnter Your Option: "))

                            if option == 1:
                                amount = int(input("\nDeposit Amount: "))
                                user.deposit(amount, bank)

                            elif option == 2:
                                amount = int(input("\nWithdraw Amount: "))
                                user.withdraw(amount, bank)

                            elif option == 3:
                                user.check_balance(bank)

                            elif option == 4:
                                amount = int(input("\nLoan Amount: "))
                                user.take_loan(amount, bank)

                            elif option == 5:
                                reciver = input("\nReciver Account No: ")
                                amount = int(input("Transfer Amount: "))
                                user.transfer_amount(reciver, amount, bank)

                            elif option == 6:
                                user.check_transaction_history(bank)

                            elif option == 7:
                                return

                            else:
                                print("\nInvalid !!")
                    else:
                        print("\nPassword is incorrect !!")
                        return
            else:
                print(f"\n{account_no} is not found !!")

        elif option == 2:
            name = input("\nEnter Your Name: ")
            email = input("Enter Your Email: ")
            password = input("Enter Your Password: ")
            Address = input("Enter Your Address: ")
            try:
                account_type = int(
                    input("Enter Your Account Type\n1. Savings / 2. Current: ")
                )
            except:
                print("\nInvalid input! Please enter a number.\n")
                continue
            if account_type == 1:
                account_type = "Savings"
            else:
                account_type = "Current"

            new_user = User(name, password, email, Address, account_type)
            new_user.create_account(new_user, bank)

        elif option == 3:
            return

        else:
            print("\nInvalid !!")


while True:
    print(f"\n$$ Welcome to the {bank.name} $$")
    print("------------------------------------\n")
    print("1. Admin")
    print("2. User")
    print("3. Exit")

    try:
        option = int(input("\nEnter Your Option: "))
    except:
        print("\nInvalid input! Please enter a number.\n")
        continue

    if option == 1:
        admin_menu()

    elif option == 2:
        user_menu()

    elif option == 3:
        print("\nThank You So Much For Visting Our Bank")
        print("--------------------------------------")
        break

    else:
        print("\nInvalid !!")
