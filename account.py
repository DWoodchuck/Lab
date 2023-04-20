class Account:
    """
    class for the object Account
    """

    def __init__(self,name) -> str:
        """

        :param name: string variable for Account_name
        """
        self.__account_name:str = name
        self.__account_balance:float = 0


    def deposit(self,amount) -> bool:
        """

        :param amount: numeric float variable for amount #
        :return: True or False bool variable
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True





    def withdraw(self,amount) -> bool:
        """

        :param amount: numeric float variable for amount #
        :return: True or False variable
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> None:
        """
        returns the amount of money in account
        :return: account_balance amount
        """
        return self.__account_balance



    def get_name(self) -> None:
        """
        returns the name on the Account
        :return: self.__account_name
        """
        return self.__account_name