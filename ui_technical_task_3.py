class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def check_balance(self):
        return f'{self.balance} lv.'



new_bank_account = BankAccount()
print(new_bank_account.balance)

