# Cyfrin 2023
# 09-05-2023
# Bhajneet Singh Bedi



"""
This will be a GUI based application, the pop up will open and 
check if internet is present. If yes then passwords will be 
uploaded on the drive linked, else it will be saved locally.
"""

from tkinter import *

def main():
    window = Tk()
    window.geometry("600x600")
    window.title("Cyfrin")
    userName = Label(window, text="User Name").pack(side=LEFT, padx=20, pady=20)
    userEntry = Entry(window, bd=5).pack(side=RIGHT, padx = 50, pady=50)
    window.mainloop()

if __name__=="__main__":
    main()

