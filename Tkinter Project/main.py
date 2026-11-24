import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500,height= 300)

#Label
my_lable = tkinter.Label(text="I am a Lable", font=("Arial",20,"bold"))
my_lable.pack(expand=1)

#*args **kwargs

def add(*args):#YOu can write *anything but remember to use *
#   *args is unlimited positional arguments , args[0] can be used inside the fxn
    Sum = 0
    for n in args:
        Sum+=n
    return Sum

def calc(n,**kwargs):
    # **kwargs means key word arguments and they store the keywords in a dictionary\
    n += kwargs["add"]
    n *= kwargs["mul"]
    print(n)


class car:
    def __init__(self,**kw):
        self.make = kw.get("make")#benifits of using get instead of [] is that it returns none if nothing is there to get, it wont give error
        self.model = kw.get("model")

my_car = car(make="Nissan" ,model="GT-R")
print(my_car.model)
print(add(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))
print(calc(2,mul=12,add=15))
window.mainloop()
