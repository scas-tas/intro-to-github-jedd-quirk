import json
import sys
import tkinter as tk
from tkinter import ttk
unhash=lambda n:n
def clearscreen():
    for widget in root.winfo_children():
        widget.destroy()
def login(u,p):
    e=False
    try:
        if s[u]==p:
            e=True
    except:pass
    clearscreen()
    tk.Label(root,text=f"Access {("Denied","Granted")[e]}!").pack()
    tk.Button(root,text="Home",command=home).pack()
def signin():
    clearscreen()
    root.title("Login")
    tk.Button(root,text="Back",command=home).pack()
    tk.Label(root,text="Username:").pack()
    entry1 = tk.Entry(root)
    entry1.pack()
    tk.Label(root,text="Password:").pack()
    entry2 = tk.Entry(root)
    entry2.pack()
    tk.Button(root,text="Sign In",command=lambda:login(str(entry1.get()),str(entry2.get()))).pack()
def createaccount(u,p):
    e=True
    if u in s:e=False
    else:s.update({u:p})
    clearscreen()
    tk.Label(root,text=f"Account Creation {("Failed","Successful")[e]}!").pack()
    tk.Button(root,text="Home",command=home).pack()
def signup():
    clearscreen()
    root.title("Sign Up")
    tk.Button(root,text="Back",command=home).pack()
    tk.Label(root,text="Username:").pack()
    entry1 = tk.Entry(root)
    entry1.pack()
    tk.Label(root,text="Password:").pack()
    entry2 = tk.Entry(root)
    entry2.pack()
    tk.Button(root,text="Create Account",command=lambda:createaccount(str(entry1.get()),str(entry2.get()))).pack()
def home():
    clearscreen()
    root.title("Login Or Sign Up")
    tk.Label(root,text="Sign in or create an account!").pack()
    tk.Button(root,text="Sign In",command=lambda:signin()).pack()
    tk.Button(root,text="Sign Up",command=lambda:signup()).pack()
root,s = tk.Tk(),json.load(open("passwords.json","r"))
home()
root.mainloop()
json.dump(s,open("passwords.json","w"))
sys.exit()