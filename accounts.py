class Account:

    def __init__(self,name):
        self.__account_name = name
        self.__account_balance = 0


    def deposit(self,amount):
        if self.__amount <= 0:
            False
        else:
            self.__account_balance += self.__amount
            True




    def withdraw(self,amount):
        if self.__amount <= 0 or self.__amount > self.__account_balance:
            False
        else:
            self.account_balance -= self.__amount
            True

    def get_balance(self):
        return self.__account_balance



    def get_name(self):
        return name

