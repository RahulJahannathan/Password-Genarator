from tkinter import *
from random import randint

root=Tk()
root.title("Password Genarator")
root.geometry("500x300")

def generator():
    password.delete(0,END)

    passwordLength=int(Input.get())
    temp_password=''

    for i in range(passwordLength):
        temp_password+=chr(randint(33,126))
    
    password.insert(0,temp_password)
def copy():
    root.clipboard_clear()
    root.clipboard_append(password.get())

lf=LabelFrame(root,text="Length of Password?")
lf.pack(pady=20)

Input=Entry(lf,font=("Helvatica",24))
Input.pack(pady=20,padx=20)
password=Entry(root,text='',font=("Helvatica",24),bd=0,bg="systembuttonface")
password.pack(pady=20)

display=Frame(root)
display.pack(pady=20)

Buttons=Button(display,text="Generate",command=generator)
Buttons.grid(row=0,column=0,padx=10)

copyButton=Button(display,text="Copy",command=copy)
copyButton.grid(row=0,column=1,padx=10)
root.mainloop()