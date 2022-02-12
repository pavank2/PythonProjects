class Account:
    def __init__(self,filepath):
        with open(filepath,'r') as file:
            self.balance = int(file.read())

    def commit(self,filepath):
        with open(filepath,'w') as file:
            file.write(str(self.balance))

    def withdraw (self,amount):
        self.balance=self.balance - amount

       
    def deposit(self,amount):
        self.balance=self.balance + amount
    
    
    


account=Account("balance.txt")
account.withdraw(100)
account.commit("balance.txt")

