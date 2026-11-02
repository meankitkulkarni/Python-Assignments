class BankAccount:
    def __init__(self, holder, account_number, opening_balance=0.0):
        self.holder = holder
        self.account_number = account_number
        self._balance = float(opening_balance)


account1 = BankAccount("Asha", "BA101", 1500)

print(account1.holder)
print(account1.account_number)
print(account1._balance)


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

    def __str__(self):
        return f"BankAccount({self.holder}, balance=₹{self._balance:.2f})"

    def __repr__(self):
        return (
            f"BankAccount(holder={self.holder!r}, "
            f"account_number={self.account_number!r}, "
            f"opening_balance={self._balance!r})"
        )

    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented

        return self._balance + other._balance

account1 = BankAccount("Asha", "BA101", 1500)
account2 = BankAccount("Kabir", "BA102", 500)

account1.deposit(250)
account2.withdraw(100)

print(account1)
print(repr(account1))

print("Account 1 balance:", account1.get_balance())
print("Account 2 balance:", account2.get_balance())

print("Combined balance:", account1 + account2)



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

    def __str__(self):
        return f"BankAccount({self.holder}, balance=₹{self._balance:.2f})"

    def __repr__(self):
        return (
            f"BankAccount(holder={self.holder!r}, "
            f"account_number={self.account_number!r}, "
            f"opening_balance={self._balance!r})"
        )

    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self._balance + other._balance


account1 = BankAccount("Asha", "BA101", 1500)
account2 = BankAccount("Kabir", "BA102", 500)

account1.deposit(250)
account2.withdraw(100)

print("--- Normal Transactions ---")
print(account1)
print(account2)
print("Account 1 balance:", account1.get_balance())
print("Account 2 balance:", account2.get_balance())

print("\n--- Invalid Operation Tests ---")
try:
    account1.deposit(0)
except ValueError as error:
    print("Deposit error:", error)

# Test withdrawal exceeding balance
try:
    account2.withdraw(1000)
except ValueError as error:
    print("Withdrawal error:", error)

# Display dunder methods
print("\n--- Dunder Methods ---")
print("String:", str(account1))
print("Representation:", repr(account1))
print("Combined balance:", account1 + account2)
