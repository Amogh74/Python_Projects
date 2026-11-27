# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
window = Tk()
window.title("Password Manager")
window.config(padx= 50,pady=50)
lock_image = PhotoImage(file ="logo.png")
canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image = lock_image)
canvas.grid(column=1,row=0)

#Labels
website_label =Label(text="Website:")
website_label.grid(row=1,column=0)
email_label =Label(text="Email/username:")
email_label.grid(row=2,column=0)
password_label =Label(text="Password:")
password_label.grid(row=3,column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row= 1 ,column= 1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row= 2,column= 1,columnspan=2)
email_entry.insert(0,"indikaramogh@gmail.com")#0 means that string is added at the starting of the text box, we can use END to add string after something is written
password_entry = Entry(width=25)
password_entry.grid(row=3,column=1)

#Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3,column=2,columnspan=2)
add_button = Button(text="Add",width=36)
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()
