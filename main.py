from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = ("Courier", 30, "normal")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    # TImer resets to 0
    global reps
    reps = 0
    window.after_cancel(str(timer))
    timer_label.config(text="TImer", fg=GREEN, font=FONT_NAME)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:  # 8th rep is time for long break
        timer_label.config(text="Break", fg=RED, bg=YELLOW, font=FONT_NAME)
        count_down(long_break_sec)
    elif reps % 2 == 0:  # Every even rep is short break
        timer_label.config(text="Break", fg=PINK, bg=YELLOW, font=FONT_NAME)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=FONT_NAME)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    no_of_min = math.floor(count / 60)
    no_of_sec = count % 60

    if no_of_sec < 10:
        no_of_sec = f"0{no_of_sec}"

    canvas.itemconfig(timer_text, text=f"{no_of_min}:{no_of_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checks = ""
        for _ in range(math.floor(reps / 2)):
            checks += "✅"
        check_mark.config(text=checks, fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=FONT_NAME)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tom_photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tom_photo)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=FONT_NAME)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=timer_reset)
reset_button.grid(column=2, row=2)

check_mark = Label(bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
