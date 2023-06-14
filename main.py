# Cyfrin 2023
# 09-05-2023
# Bhajneet Singh Bedi



"""
This will be a GUI based application, the pop up will open and 
check if internet is present. If yes then passwords will be 
uploaded on the drive linked, else it will be saved locally.
"""

import os
import base64
import csv
import tkinter as tk
from tkinter import *
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.hazmat.primitives.kdf.pbkdf2.PBKDF2HMAC import derive


def main():
    # Making every content global so that it can be accessed later on in every function.
    global window, btn, userName, userNameEntry, userPass, userPassEntry, addps, getPs, addName, addNameEntry, addPassword, addPassEntry, secretPass, secretPassEntry, submitAdd, secPass, secPassEntry
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
    # getPs = Button(window, text="See Saved Password", command = getPass)

    ######### Add pass content #########
    addName = Label(window, text="Add web link")
    addNameEntry = Entry(window, bd=5)
    addPassword = Label(window, text="Enter Password")
    addPassEntry = Entry(window, bd=5)
    secretPass = Label(window, text="Your Secret Password")
    secretPassEntry = Entry(window, bd=5)
    submitAdd = Button(window, text='Add Password', command=addpsButton)

    ######### Get Pass content #########
    # secPass = Label(window, text='Enter secret Password')
    # secPassEntry = Entry(window, bd=5)


    # print(os.getcwd())
    # os.chdir('C:')
    # print(os.getcwd())
    # print(os.listdir())
    window.mainloop()


def Page1():
    global usNaEn, usPaEn
    # Getting username and pass.
    usNaEn = userNameEntry.get()
    usPaEn = userPassEntry.get()


    # Making essential files.
    if not os.path.isdir('Cyfrin'):
        os.mkdir('Cyfrin')
    os.chdir('Cyfrin')
    
    ########### Usernames and password file
    # if not os.path.isfile('Username.csv'):
    #     f = open('username.csv','w')
    #     writer=csv.writer(f)
    #     writer.writerow(['Username', 'Password'])
    #     f.close()
    #######################################

    # Individual files.
    if not os.path.isfile(usNaEn+'.csv'):
        f = open(usNaEn+'.csv','w')
        writer=csv.writer(f)
        writer.writerow(['Web Link', 'Password', 'Secret Password'])
        f.close()

    
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
        # getPs.place(relx=.5, rely=.5,anchor= CENTER)
    else:
        tk.messagebox.showinfo("Error", "The username or password is incorrect!!")


    # Creating a directory for user's info and weblink and passwords directory.
    # os.chdir("C:")

    # os.mkdir(usNaEn)
    # os.chdir(usNaEn)
    # print(os.getcwd())
    # Main folder


def addPass():
    # This function includes add pass functionality.
    # delete all content
    addps.destroy()
    # getPs.destroy()
    # Add the website link
    addName.place(relx=.408, rely=.4,anchor= CENTER)
    addNameEntry.place(relx=.6, rely=.4,anchor= CENTER)

    # Add the password
    addPassword.place(relx=.4, rely=.5,anchor= CENTER)
    addPassEntry.place(relx=.6, rely=.5,anchor= CENTER)

    # Add secret Password
    secretPass.place(relx=.37, rely=.6,anchor= CENTER)
    secretPassEntry.place(relx=.6, rely=.6,anchor= CENTER)

    # Submit button to add password
    submitAdd.place(relx=.5, rely=.7,anchor= CENTER)




def addpsButton():
    # Encrypting
    webLink = addNameEntry.get()
    webPassword = addPassEntry.get()
    secPass = secretPassEntry.get()

    # f = open(usNaEn+'.csv','w')
    # writer=csv.writer(f)
    # writer.writerow(['Web Link', 'Password'])
    # f.close()

    
    encWebPassword = encrypt(webPassword, secPass)
    print(type(encWebPassword))
    encSecPassword = encrypt(secPass, secPass)
    # Now we have the password and file now let's save it.
    # os.chdir('Cyfrin')
    # print(os.getcwd())
    with open(usNaEn+'.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow([webLink, encWebPassword, encSecPassword])
    # print(encWebLink,"\t",encWebPassword)
    
    # print(decrypt(encWebLink,secPass),"\t",decrypt(encWebPassword,secPass))
    # Destroying
    addName.destroy()
    addNameEntry.destroy()
    addPassword.destroy()
    addPassEntry.destroy()
    secretPass.destroy()
    secretPassEntry.destroy()
    submitAdd.destroy()
    Label(window, text="Password successfully added", font=20).place(relx=0.5, rely=0.5, anchor=CENTER)
    quitButton = Button(window, text="Quit", command=quitWindow)
    quitButton.place(relx=.5, rely=.6,anchor= CENTER)


def encrypt(message, password):
    salt = b'\x9d\xae\xd7\xaa\xc9\x1eG\xa3B\xa8\xeb\xa0\xf8\xed'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(message.encode())
    return cipher_text


def decrypt(cipher_text, password):
    salt = b'\x9d\xae\xd7\xaa\xc9\x1eG\xa3B\xa8\xeb\xa0\xf8\xed'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    cipher_suite = Fernet(key)
    plaintext = cipher_suite.decrypt(cipher_text)
    return plaintext.decode()


def quitWindow():
    window.destroy()

# def getPass():
#     addps.destroy()
#     getPs.destroy()
#     secPass.place(relx=0.4, rely=0.5, anchor=CENTER)
#     secPassEntry.place(relx=0.65, rely=0.5, anchor=CENTER)
#     secGetPass = secPassEntry.get()

#     with open(usNaEn+'.csv','r') as file:
#         reader = csv.DictReader(file)
#         pss = []
#         for row in reader:
#             pss.append(row['Secret Password'])
#         # print(bytes(pss[0], 'utf-8'))
#         # print(type(bytes(pss[0], 'utf-8')))
#     if secGetPass == decrypt(pss[0], secGetPass):
#         with open(usNaEn+'.csv','r') as file:
#             reader = csv.DictReader(file)
#             values=[]
#             for row in reader:
#                 value = row['Password']
#                 values.append(value)
    


if __name__=="__main__":
    main()