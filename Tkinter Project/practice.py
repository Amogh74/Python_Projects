    my_label.config(text= new_text)


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=500)
window.config(padx=100,pady=100)#used to add space
#Label
my_label = Label(text="This is old text",font=("Arial" , 20,"bold"))
my_label.config(text="This is new text")
#my_label.place(x=0,y=0)#places the text at this location
#better method:-
my_label.grid(column=0,row=0) #This is starting position , this will be taken as refrence for other .grid()

#Note :  cannot use pack() and grid() together


#button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1,row=1)
#challenge:lect no 211
new_button = Button(text="New_ME",command=button_clicked)
new_button.grid(column=2,row=0)
#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3,row=2)


window.mainloop()
