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
import os
import pandas as pd
import hashlib
def main():
    # Making every content global so that it can be accessed later on in every function.
    global window, btn, userName, userNameEntry, userPass, userPassEntry, addps, getPs, addName, addNameEntry, addPassword, addPassEntry, submitAdd
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
    # This is the page 2 content.
    addps = Button(window, text="Add new password", command=addPass)
    getPs = Button(window, text="See Saved Password", command = getPass)

    ######### Add pass content #########
    addName = Label(window, text="Add web link")
    addNameEntry = Entry(window, bd=5)
    addPassword = Label(window, text="Enter Password")
    addPassEntry = Entry(window, bd=5)
    submitAdd = Button(window, text='Add Password', command=addpsButton)
    # print(os.getcwd())
    # os.chdir('C:')
    # print(os.getcwd())
    # print(os.listdir())
    window.mainloop()


def Page1():
    # Getting username and pass.
    usNaEn = userNameEntry.get()
    usPaEn = userPassEntry.get()
    
    # checking username and pass
    if (usNaEn == 'b' and usPaEn == '1'):
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


def addPass():
    # This function includes add pass functionality.
    # delete all content
    addps.destroy()
    getPs.destroy()
    # Add the website link
    addName.place(relx=.4, rely=.4,anchor= CENTER)
    addNameEntry.place(relx=.6, rely=.4,anchor= CENTER)

    # Add the password
    addPassword.place(relx=.4, rely=.5,anchor= CENTER)
    addPassEntry.place(relx=.6, rely=.5,anchor= CENTER)

    # Submit button to add password
    submitAdd.place(relx=.5, rely=.6,anchor= CENTER)




def addpsButton():
    # Encrypting
    webLink = addNameEntry.get()
    webPassword = addPassEntry.get()
    encWebLink = encrypted(webLink)
    encWebPassword = encrypted(webPassword)

    print(encWebLink, encWebPassword)
    # Destroying
    addName.destroy()
    addNameEntry.destroy()
    addPassword.destroy()
    addPassEntry.destroy()
    submitAdd.destroy()
    Label(window, text="Password successfully added", font=20).place(relx=0.5, rely=0.5, anchor=CENTER)
    quitButton = Button(window, text="Quit", command=quitWindow)
    quitButton.place(relx=.5, rely=.6,anchor= CENTER)


def encrypted(message):
    sha256 = hashlib.sha256()
    sha256.update(message.encode('utf-8'))
    encrypted_message = sha256.hexdigest()
    return encrypted_message

def quitWindow():
    window.destroy()

def getPass():
    # os.chdir("C:")
    if not os.path.isfile('cyfrin.csv'):
        df=pd.DataFrame(columns=["Web Link", "Passwords"])
        df.to_csv('cyfrin.csv', index=False)
    else:
        df=pd.read_csv('cyfrin.csv')
            # writer = csv.writer(file)
            # field = ["name", "age", "country"]
            
            # writer.writerow(field)
            # writer.writerow(["Oladele Damilola", "40", "Nigeria"])
            # writer.writerow(["Alina Hricko", "23", "Ukraine"])
            # writer.writerow(["Isabel Walter", "50", "United Kingdom"])






if __name__=="__main__":
    main()