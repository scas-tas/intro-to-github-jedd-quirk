import random as r

class Account:
    def __init__(self, number, balance, owner):
        self.number = number
        self.balance = balance
        self.owner = owner
    def deposit(self, amount):
        self.balance+=amount
        return f"Successfully deposited {amount}. Your new balance is {self.balance}"
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
            return f"Successful withdrew {amount}, your balance is now {self.balance}."
        else:
            return f"Could not withdraw {amount} from your account because of insufficient funds! You can only withdraw {self.balance}."
    def gamble(self, amount):
        if r.random()>0.80:
            self.balance+=amount
        else:
            self.balance-=amount
    def checkbalance(self):
        return f"Your current balance is {self.balance}."

def bankwelcome():
    return input("Welcome to Bank Python! How can I help you today? ")
n=bankwelcome()
accounts=[]
while n.lower()!="quit":
    match n.lower():
        case "newaccount":
            newn=r.randint(0,9999)
            accounts.append(Account(newn,float(input("Starting Balance: ")),input("Name: ")))
            print(f"Your new account's number is {newn}")
        case "deposit":
            dn = int(input("Number: "))
            for i in accounts:
                if i.number==dn:
                    da=float(input("Amount:"))
                    print(i.deposit(da))
        case "seebal":
            bn=int(input("Number: "))
            for i in accounts:
                if i.number==dn:
                    print(i.checkbalance())
    n=input("Anything Else? ")