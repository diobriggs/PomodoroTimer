import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text = "00:00")
    timer_label.config(text = "Timer", fg = GREEN)
    checkmark_label.config(text="")
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 2 != 0:
        count_down(work_sec)
        timer_label.config(text = "Work", fg = GREEN)
    elif REPS % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg = RED )
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg = PINK)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global REPS
    mins = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text = f"{mins}:{seconds}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(REPS//2):
            marks += "✓"
        checkmark_label.config(text= marks)




# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg= YELLOW)


canvas = tkinter.Canvas(width = 200, height = 224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file= "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text= "00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)


timer_label = tkinter.Label(text = "Timer", bg = YELLOW, fg = GREEN, font=(FONT_NAME, 35))
timer_label.grid(column = 1, row = 0)

checkmark_label = tkinter.Label(bg = YELLOW, fg = GREEN, font=(FONT_NAME, 35))
checkmark_label.grid(column = 1, row = 3)

start_button = tkinter.Button(text = "Start", highlightthickness=0, highlightbackground=YELLOW, command= start_timer)
start_button.grid(column = 0, row = 2)

reset_button = tkinter.Button(text = 'Reset', highlightthickness=0,highlightbackground=YELLOW, command = reset_timer)
reset_button.grid(column = 2, row = 2)






window.mainloop()