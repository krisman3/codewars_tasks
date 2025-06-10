class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f'{amount} lv. deposited!'

    def withdraw(self, amount):
        if amount > self.balance:
            return f'Insufficient funds!'
        else:
            self.balance -= amount
            return f'{amount} lv. withdrawn. New balance: {self.balance}'

    def check_balance(self):
        return f'{self.balance} lv.'


new_bank_account = BankAccount()
print(new_bank_account.deposit(15))
print(new_bank_account.withdraw(14))
print(new_bank_account.balance)
