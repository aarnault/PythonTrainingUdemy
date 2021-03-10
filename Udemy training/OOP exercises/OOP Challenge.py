class Account():
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__ (self):
        return(f'Account owner: {self.owner} and Account balance: {self.balance}')

    def deposit (self, amount1):
        self.balance += amount1
        print ("The amount {} has been added to your account". format(amount1))

    def withdraw (self, amount2):
        if self.balance >= amount2:
            self.balance -= amount2
            print('The withdraw has been accepted')
        else:
            print("The withdraw cannot be done as not enough money are on the account")

acct1 = Account('Jose',100)

print(acct1)
acct1.owner
acct1.balance

acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)