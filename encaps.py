class Bank:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return f"Your Balance is {self.__balance}"
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"you have credited your bank account with {amount} and your balance is now {self.__balance}"
        else:
            return f"you can only enter a positive number"
    
    def withdraw(self, amount):
        if amount > 0:
            self.__balance -= amount
            return f"you have withdrawn {amount} and your balance is {self.__balance}"
        else:
            return f"you can only withdraw a positive number"  

acc = Bank('2104369827', 10)
# print(acc.get_balance())
# print(acc.deposit(100))
print(acc.get_balance())
print(acc.withdraw(10))
print(acc.get_balance())