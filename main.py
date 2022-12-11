from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
        global reps
        reps += 1

        if reps % 8 == 0:
            countdown(LONG_BREAK_MIN*60)
            label.config(text="Long Break", fg=RED)

        elif reps % 2 == 0:
            countdown(SHORT_BREAK_MIN*60)
            label.config(text="Short Break", fg=PINK)

        else:
            countdown(WORK_MIN*60)
            label.config(text="Work", fg=GREEN)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):

    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count -1)
    else:
        start_timer()
        marks = " "
        work_season = math.floor(reps/2)
        for _ in range(work_season):
            marks += "✔"
        check.config(text= marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx= 100 , pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
canvas.grid(column= 1 , row= 1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 33, "bold"))


label = Label()
label.config(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label.grid(column= 1 , row= 0)

start = Button()
start.config(text="Start", width=8, bg=GREEN,command=start_timer)
start.grid(column=0, row=3)

reset = Button()
reset.config(text="Reset", width=8, bg=GREEN, command=reset_timer)
reset.grid(column=3, row=3)

check = Label()
check.grid(column=1, row=4)




window.mainloop()


