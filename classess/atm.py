# creating a new class
# read on principles of OOP
class Bank:
    name = "Equity"

class ATMCard(Bank):
    # Bank.name =
    # this is a property
    # a class variable / data member
    #  a class variable is shared among all instances ofclass
    colour = "Brown"
    balance = 0

    # actions are called methods
    # methods are just functions,only that they are inside a class


    # a construcotr is a special method that runs everytime you instantiate
    # in python
    def __init__(self,op_balance):
        self.balance = op_balance



    def deposit(self,amount):
        self.balance += amount
        print("Deposited ",amount)

    def withdraw(self,amount):
        if self.balance < amount:
            print("Sorry Insufficient")
        else:
            self.balance -= amount
            print("Success:{}".format(amount))


