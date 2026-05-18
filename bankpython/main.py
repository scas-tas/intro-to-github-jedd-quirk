import random as r
#import tkinter as tk
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
        if amount<=self.balance:
            if r.random()>0.80:
                self.balance+=amount
                return f"You win! Your new balance is {self.balance}."
            else:
                self.balance-=amount
                return f"You lose! Your new balance is {self.balance}."
        else:
            return "Insufficient funds!"
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
                    da=float(input("Amount: "))
                    print(i.deposit(da))
        case "seebal":
            bn=int(input("Number: "))
            for i in accounts:
                if i.number==bn:
                    print(i.checkbalance())
        case "withdraw":
            wn=int(input("Number:"))
            for i in accounts:
                if i.number==wn:
                    wa=float(input("Amount: "))
                    print(i.withdraw(wa))
        case "gamble":
            gn=int(input("Number:"))
            for i in accounts:
                if i.number==gn:
                    ga=float(input("Amount: "))
                    print(i.gamble(ga))
    n=input("Anything Else? ")