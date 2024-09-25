from tkinter import *
import pandas
from random import choice
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
timer = None
current_card = {}

# Get the data from csv file
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    words_data = data.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(card_image, image=logo_back)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(words_data)
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(card_image, image=logo_front)
    flip_timer = window.after(3000, flip_card)


def remove_word():
    words_data.remove(current_card)
    to_learn = pandas.DataFrame(words_data)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
logo_back = PhotoImage(file="./images/card_back.png")
logo_front = PhotoImage(file="./images/card_front.png")
card_image = canvas.create_image(400, 263, image=logo_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 120, text="Title", font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=3)


# Buttons
my_image1 = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=my_image1, command=next_card)
wrong_button.config(highlightthickness=0)
wrong_button.grid(row=1, column=0)

my_image2 = PhotoImage(file="./images/right.png")
right_button = Button(image=my_image2, command=remove_word)
right_button.config(highlightthickness=0)
right_button.grid(row=1, column=2)
messagebox.showinfo(title="Info", message="For each card you will get the word in English after 3 seconds"
                                          "Press right button if you know the word otherwise press the left button")

next_card()


window.mainloop()
