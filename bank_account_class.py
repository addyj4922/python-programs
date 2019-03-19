class Account:
    def __init__(self,owner,balance=100):
        self.owner=owner
        self.balance=balance
    def deposit(self,deposit):
        print("Deposit of {} Accepted".format(deposit))
        self.balance=self.balance+deposit

    def withdraw(self,withdraw):
        if self.balance>=withdraw:
            print("Withdrawal of {} Accepted!".format(withdraw))
            self.balance=self.balance-withdraw
        else:
            print("Sorry not enough Funds\nWithdrawal rejected!!")
    def __str__(self):
        return "Owner: {} \nBalance: {}".format(self.owner,self.balance)
a=Account('Addy',500)
a.deposit(100)
a.withdraw(2345)
print(a)