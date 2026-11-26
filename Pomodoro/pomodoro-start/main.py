#                                                    EVENT DRIVEN GUI
from tkinter import *
import math
#  ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FA699E"
RED =   "#e7305b"               #"#e7305b"
NAVY_BLUE = "#1B365D"
GREEN = "#167D8D"               #"#9bdeac"
YELLOW = "#B9E4E8"              #"#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

window = Tk()
window.title("Pomodoro")#pomodoro means tomato in Italy
window.config(padx=100,pady=50,bg=YELLOW)

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(Timer_text,text ="00:00")
    title_label.config(text="Timer")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    #TODO: 1. If it is the 1st/3'rd/5th.. rep then countdown(work_time)
    #TODO: 2. if it is 8th rep then long Break
    #TODO: 2. if it is 2'nd/4th/6th.... rep then short Break
    work_time = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    if reps%8==0:
        count_down(long_break)
        title_label.config(text="Break!!",fg=RED,bg=YELLOW)
        reps+=1
    elif reps%2 == 0:
        count_down(short_break)
        title_label.config(text="Break!!", fg=PINK, bg=YELLOW)
        reps+=1
    else:
        count_down(work_time)
        title_label.config(text="Work Time", fg=NAVY_BLUE, bg=YELLOW)
        reps+=1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = math.floor(count/60)
    count_sec = count%60

#   Dynamic Typed , means that we can dynamically chang the data type , example below
    #ie we converted  int variable into string type variable
    if count_sec <10:
        count_sec = f"0{count_sec}"

    if count_minute <10:
        count_minute = f"0{count_minute}"

    canvas.itemconfig(Timer_text,text = f"{count_minute}:{count_sec}")
    if count > 0:
       global timer
       timer = window.after(1000,count_down,count -1) #here 100 is time in millisec , RECURSION Here
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
            tick.config(text=mark,fg=GREEN,bg=YELLOW,font=(FONT_NAME,15,"bold"))



# ---------------------------- UI SETUP ------------------------------- #


#Tkinter Canvas Widget
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100,112,image= tomato_img)#here x_cor = 100 , y_cor =112
Timer_text =canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


#Title Label
title_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,30,"bold"),bg=YELLOW)
title_label.grid(column=1,row=0)

#Start Button
start_button = Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)

#Reset Button
reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(column=2,row=2)

#Check Mark Text
tick = Label(text="✔",fg=GREEN,bg=YELLOW,font=(FONT_NAME,15,"bold"))
tick.grid(column=1,row=3)
window.mainloop()