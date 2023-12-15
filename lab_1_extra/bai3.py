class BankAccount:
    def __init__(self, account_number, account_name, balance):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def recharge(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def info(self):
        return {
            "account_number": self.account_number,
            "account_name": self.account_name,
            "balance": self.balance
        }


bank = BankAccount("123456789", "Nguyen Van A", 1000000)
bank.withdraw(500000)
print(bank.info())
