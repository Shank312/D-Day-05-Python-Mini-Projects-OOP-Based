
# Concept: Inheritance allows a child class to use or extend the behavior of a parent class.
# Use-case: Create a banking system where common features are inherited by different account types (Savings, Checking).

# Base class for all bank accounts
class BankAccount:
    def __init__(self, owner, balance = 0):
        # Attributes to store bank account owner's name and current balance
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # Add the deposit amount to the balance
        self.balance += amount
        print(f"{amount} deposited. New Balance: {self.balance}")

    def withdraw(self, amount):
        # Withdraw only if sufficient balance is available 
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. Remaining Balance: {self.balance}")
        else:
            print("Insufficient balance.")

# Subclass of BankAccount to represent a savings account
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        # Call the parent class constructor using super()
        super().__init__(owner, balance)
        # Additional attribute specific to saving account
        self.interest_rate = interest_rate

    def add_interest(self):
        # Calculate interest and add it to the balance
        interest = self.balance*self.interest_rate
        self.deposit(interest)                             # Reuse the deposit method from the parent class

# Subclass of BankAccount to represent a checking point
class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=1000):
        # Call the parent class constructor using super()
        super().__init__(owner, balance)
        # Overdraft limit allows withdrawing more than the current balance up to a limit
        self.overdraft_limit = overdraft_limit

    # Method overriding: modifies the base class withdraw behavior
    def withdraw(self, amount):
        # Allow withdrawal even if the balance is less than amount, up to the overdraft limit
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{amount} withdrawn. Remaining Balance: {self.balance}")
        else:
            print("Overdraft limit exceeded.")


# Add sample code to see output

# Create a savings account with ₹1000 balance
savings = SavingsAccount("Shankar", 1000)

# Deposit  ₹500
savings.deposit(500)

# Add interest (5% of current balance)
savings.add_interest()

# Withdraw  ₹300
savings.withdraw(300)

# Create a checking account with ₹500 balance and ₹1000 overdraft limit
checking = CheckingAccount("Shankar", 500)

# Withdraw within balance
checking.withdraw(400)

# Withdraw using overdraft
checking.withdraw(900)

# Attempt to withdraw beyond overdraft limit
checking.withdraw(300)