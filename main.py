from tkinter import *
import math

PINK = "#e2979c"
GREEN = "#9bdeac"
RED = "#e7305b"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(Timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# timer_mechanism
def start_timer():
    global reps
    reps += 1

    work_in_sec = WORK_MIN * 60
    short_break_in_sec = SHORT_BREAK_MIN * 60
    long_break_in_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_in_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_in_sec)
        title_label.config(text="Break", fg=PINK)



    else:
        count_down(work_in_sec)
        title_label.config(text="WorK", fg=GREEN)


# countDown TIMER

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(Timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer

        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✅"
        check_marks.config(text=marks)

    # UI setUP


window = Tk()
window.title("TIMER!!")

window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=600, height=624, bg=YELLOW, highlightthickness=0)
title_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)
clock_image = PhotoImage(file="timer.png")
canvas.create_image(300, 312, image=clock_image)
Timer_text = canvas.create_text(300, 312, text="00:00", fill="black", font=(FONT_NAME, 38, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="START", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="RESET", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✅", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)
window.mainloop()
