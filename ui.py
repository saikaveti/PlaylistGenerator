from tkinter import *

window = Tk()
window.title("Fuzzy Elephant")
window.configure(background="black")
logo = PhotoImage(file="logo.gif")
Label (window, image=logo, bg="black") .grid(row=0, column=0, sticky=E)
#id = window.create_rectangle(100, 100, 100, 100, fill="black")
window.mainloop()