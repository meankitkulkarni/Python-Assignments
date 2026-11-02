
class BankAccount:
    def __init__(self, holder, account_number, opening_balance=0.0):
        if not holder.strip():
            raise ValueError("Account holder cannot be blank")

        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative")

        self.holder = holder
        self.account_number = account_number
        self._balance = float(opening_balance)

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount

# Create a bank account
account1 = BankAccount("Asha", "BA101", 1500)

print("Opening balance:", account1.get_balance())

# Deposit money
account1.deposit(250)
print("After deposit:", account1.get_balance())

# Withdraw money
account1.withdraw(100)
print("After withdrawal:", account1.get_balance())
