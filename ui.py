from tkinter import *

userEntry = ""
passEntry = ""

def click():
    global userEntry, passEntry
    userEntry = username.get()
    passEntry = password.get()
    print(userEntry)
    print(passEntry)

def printU():
    print(userEntry)

window = Tk()
window.title("Fuzzy Elephant")
window.configure(background="black")
logo = PhotoImage(file="logo.gif")
Label (window, image=logo, bg="black") .grid(row=0, column=0, sticky=E)
Label (window, text = "Spotify Playlist Generator", bg="black", fg="white", font="none 30 bold") .grid(row=2, column=0, sticky=W)
Label (window, text = "Username:", bg="black", fg="white", font="none 12 bold") .grid(row=4, column=0, sticky=W)
Label (window, text = "Password:", bg="black", fg="white", font="none 12 bold") .grid(row=6, column=0, sticky=W)
username = Entry(window, width=20, bg="white")
username.grid(row=5, column=0, sticky=W)
password = Entry(window, show="*", width=20, bg="white")
password.grid(row=7, column=0, sticky=W)
Button (window, text="Log In", width = 6, command=click) .grid(row=9, column=0, sticky=W)
window.mainloop()