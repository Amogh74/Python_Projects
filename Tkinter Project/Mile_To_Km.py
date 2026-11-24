from tkinter import *
window = Tk()
window.title("Miles TO KM Converter")
window.minsize(width=200,height=100)
window.config(padx=20,pady=20)

def convert():
    miles_to_convert = float(miles.get())
    km = miles_to_convert*1.609
    kilometer_result.config(text=f"{km}")

miles = Entry(width=7)
miles.grid(column=1,row=0)


miles_txt = Label(text = "Miles")
miles_txt.grid(column=2,row=0)

is_equal_label = Label(text="is Equal to")
is_equal_label.grid(column=0,row=1)

kilometer_result = Label(text="0")
kilometer_result.grid(column=1,row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2,row=1)
#Calculate Button
calculate = Button(text="Calculate",command=convert)
calculate.grid(column=1,row=2)


window.mainloop()
