class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number # protected
        self.__balance = balance # private

    # get method for private attribute
    def get_balance(self):
        return self.__balance

    # set method for private attribute
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid Balance")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Invalid Deposit Amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Invalid Withdraw Amount")


account = BankAccount("HNB9797", 2000)
print("Initial Bank Amount :",account.get_balance())
account.set_balance(50000)
print("Updated Bank Amount :",account.get_balance())
account.deposit(90000)
print("Deposited Bank Amount :",account.get_balance())
account.withdraw(70000)
print("Withdraw Bank Amount :",account.get_balance())




