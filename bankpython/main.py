import random as r
import tkinter as tk
import sys
class Account:
    def __init__(self, number, balance, owner):
        self.number = number
        self.balance = balance
        self.owner = owner
    def deposit(self, amount):
        self.balance+=amount
        return f"Successfully deposited {amount}. Your new balance is {self.balance}."
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

accounts=[]
def clearscreen():
    for widget in root.winfo_children():
        widget.destroy()
def accountconfirm(entered):
    accnum=len(accounts)
    accounts.append(Account(accnum,0.00,entered))
    popup=tk.Toplevel()
    tk.Label(popup,text=f"New Account for {entered} with the number {accnum}.").pack()
    tk.Button(popup,text="Done",command=home).pack()
def newaccount():
    clearscreen()
    tk.Label(root,text="Name:").pack()
    entry = tk.Entry(root)
    entry.pack()
    tk.Button(root,text="Enter",command=lambda: accountconfirm(str(entry.get()))).pack()
def depositconfirm(amount,accnum):
    fail=True
    clearscreen()
    for account in accounts:
        if account.number==accnum:
            fail=False
            tk.Label(root,text=account.deposit(amount)).pack()
            tk.Button(root,text="Done",command=home).pack()
    if fail:
        tk.Label(root,text="Failed to deposit, account does not exist.").pack()
        tk.Button(root,text="Done",command=home).pack() 
def deposit():
    clearscreen()
    tk.Label(root,text="Deposit Amount:").pack()
    entry1 = tk.Entry(root)
    entry1.pack()
    tk.Label(root,text="Account Number:").pack()
    entry2 = tk.Entry(root)
    entry2.pack()
    tk.Button(root,text="Enter",command=lambda: depositconfirm(float(entry1.get()),int(entry2.get()))).pack()
def withdrawconfirm(amount,accnum):
    fail=True
    clearscreen()
    for account in accounts:
        if account.number==accnum:
            fail=False
            tk.Label(root,text=account.withdraw(amount)).pack()
            tk.Button(root,text="Done",command=home).pack()
    if fail:
        tk.Label(root,text="Failed to withdraw, account does not exist.").pack()
        tk.Button(root,text="Done",command=home).pack() 
def withdraw():
    clearscreen()
    tk.Label(root,text="Withdraw Amount:").pack()
    entry1 = tk.Entry(root)
    entry1.pack()
    tk.Label(root,text="Account Number:").pack()
    entry2 = tk.Entry(root)
    entry2.pack()
    tk.Button(root,text="Enter",command=lambda: withdrawconfirm(float(entry1.get()),int(entry2.get()))).pack()
def gambleconfirm(amount,accnum):
    fail=True
    clearscreen()
    for account in accounts:
        if account.number==accnum:
            fail=False
            tk.Label(root,text=account.gamble(amount)).pack()
            tk.Button(root,text="Done",command=home).pack()
    if fail:
        tk.Label(root,text="Failed to gamble, account does not exist.").pack()
        tk.Button(root,text="Done",command=home).pack()
def gamble():
    clearscreen()
    tk.Label(root,text="Gamble Amount:").pack()
    entry1 = tk.Entry(root)
    entry1.pack()
    tk.Label(root,text="Account Number:").pack()
    entry2 = tk.Entry(root)
    entry2.pack()
    tk.Button(root,text="Enter",command=lambda: gambleconfirm(float(entry1.get()),int(entry2.get()))).pack()
def home():
    clearscreen()
    root.title("Bank Python")
    tk.Label(root,text="Welcome to Bank Python").pack()
    tk.Button(root,text="New Account",command=newaccount).pack()
    tk.Button(root,text="Deposit",command=deposit).pack()
    tk.Button(root,text="Withdraw",command=withdraw).pack()
    tk.Button(root,text="Gamble",command=gamble).pack()
root = tk.Tk()
home()
root.mainloop()
print(len(accounts))
sys.exit()