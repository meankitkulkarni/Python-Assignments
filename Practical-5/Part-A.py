class BankAccount:
    def __init__(self, holder, account_number, opening_balance=0.0):
        self.holder = holder
        self.account_number = account_number
        self._balance = float(opening_balance)


account1 = BankAccount("Asha", "BA101", 1500)

print(account1.holder)
print(account1.account_number)
print(account1._balance)