from tkinter.messagebox import showerror


a = 2 if 3!=1 else 0
print(a)

def emailIsValid(email):
    return "@" in email

def save_user():
    return "user saved"

def raiseError():
    return "invalid email"

print(save_user() if emailIsValid("halil@hasmer.com") else raiseError())