class BankAccount:
    def __init__(self, int_rate = .02, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Interest Rate: {self.int_rate}, {self.balance}")
        return self
        
    def yield_interest(self):
        self.balance = int_rate * balance
        return self

# create 2 accounts
first_acct = BankAccount(.25, 1000)
second_acct = BankAccount(.09, 2000)
print(first_acct.int_rate)
# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
first_acct.deposit(20500).deposit(150).deposit(125).withdraw(250)
# first_acct.yield_interest()
first_acct.display_account_info()
# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
second_acct.deposit(1000).deposit(2000).withdraw(400).withdraw(300).withdraw(200).withdraw(100).display_account_info()