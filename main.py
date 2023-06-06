# Cyfrin 2023
# 09-05-2023
# Bhajneet Singh Bedi



"""
This will be a GUI based application, the pop up will open and 
check if internet is present. If yes then passwords will be 
uploaded on the drive linked, else it will be saved locally.
"""

from tkinter import *
import tkinter as tk
import tkinter.messagebox

ctr=0

def main():
    # Making every content global so that it can be accessed later on in every function.
    global btn, userName, userNameEntry, userPass, userPassEntry, ctr, addps, getPs, btn1
    window = Tk()
    window.geometry("600x600")
    frame=Frame(window)
    frame.place(relx=0.5)
    window.title("Cyfrin")
    
    # This is the page 1.
    userName = Label(window, text="User Name")
    userName.place(relx=.4, rely=.4,anchor= CENTER)
    userNameEntry = Entry(window, bd=5)
    userNameEntry.place(relx=.6, rely=.4,anchor= CENTER)


    userPass = Label(window, text="Password")
    userPass.place(relx=.4, rely=.5,anchor= CENTER)
    userPassEntry = Entry(window, bd=5)
    
    userPassEntry.place(relx=.6, rely=.5,anchor= CENTER)
    
    btn = Button(window,text ="Submit",command = Page1)
    btn.place(relx=.5, rely=.6,anchor= CENTER)
    btn1 = Button(window, text='Back', command=back2one)
    # This is the page 2 content.
    addps = Button(window, text="Add new password", command=addPass)
    getPs = Button(window, text="See Saved Password", command = getPass)
    btn1 = Button(window, text='Back', command=back2one)


    window.mainloop()


def Page1():
    # Getting username and pass.
    usNaEn = userNameEntry.get()
    usPaEn = userPassEntry.get()

    # checking username and pass
    if (usNaEn == 'bhajneet' and usPaEn == '123456'):
        # Destroying first screen objects.
        userName.destroy()
        userNameEntry.destroy()
        userPass.destroy()
        userPassEntry.destroy()
        btn.destroy()

        # Displaying second screen objects.
        addps.place(relx=.5, rely=.4,anchor= CENTER)
        getPs.place(relx=.5, rely=.5,anchor= CENTER)
    else:
        tk.messagebox.showinfo("Error", "The username or password is incorrect!!")

def getPass():
    pass


def addPass():
    pass


def back2one():
    """"
    addps.destroy()
    getPs.destroy()
    btn1.destroy()
    """
    pass



if __name__=="__main__":
    main()