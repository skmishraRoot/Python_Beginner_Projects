from tkinter import *
import random
import pyperclip
import string



# Setting up tkinter window
root = Tk()
root.geometry("600x300")
root.title("Password Generator")



#setting up tkinter varibales
passstr = StringVar()
passlen = IntVar()
passlen.set(0)



# Generate password
def generate():
    pass_len=passlen.get()
    ran = ''.join(random.choices(string.ascii_uppercase+ string.ascii_lowercase + string.digits, k=pass_len))    
    password = ran
    passstr.set(password)



# Copy to clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)



# Heading for the application
Label(root, text="Password Generator Application", font="calibri 20 bold").pack()
# label for length of the password
Label(root, text="Enter password length", font="calibri 17").pack(pady=3)
# Input area for length
Entry(root, textvariable=passlen, width=10, font='bold').pack(pady=3)
# Button to call genarate function and create password
Button(root, text="Generate Password" ,font="calibri 15", command=generate).pack(pady=7)
# area to show password
Entry(root, textvariable=passstr, font='bold').pack(pady=3)
# button to copy password
Button(root, text="Copy to clipboard",font="calibri 15", command=copytoclipboard).pack()



# calling mainloop
root.mainloop()
