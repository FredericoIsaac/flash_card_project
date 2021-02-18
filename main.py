from tkinter import *
from tkinter import messagebox
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
exercise_word = {}
words, words_translation = None, None

# ---------------------------- HANDLE DATA ------------------------------- #


def open_dictionary():
    global words, words_translation
    try:
        words = pandas.read_csv("./data/words_to_learn.csv")
    except FileNotFoundError:
        words = pandas.read_csv("./data/french_words.csv")
    finally:
        words_translation = words.to_dict(orient="records")

# ---------------------------- RIGHT OR WRONG ANSWER ------------------------------- #


def right_answer():
    words_translation.remove(exercise_word)
    df = pandas.DataFrame(words_translation)
    df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def wrong_answer():
    next_card()

# ---------------------------- FLIP CARD MECHANISM ------------------------------- #


def next_card():
    global exercise_word, flip_timer
    window.after_cancel(flip_timer)

    try:
        exercise_word = random.choice(words_translation)
    except IndexError:
        reset_game = messagebox.askyesno(title="Congrats!!", message="You know all the words! \n"
                                                                     "Do you want reset the words?")
        if reset_game:
            os.remove("./data/words_to_learn.csv")
            open_dictionary()

    canvas.itemconfig(language_indication, text="French", fill="black")
    canvas.itemconfig(word_translate, text=f"{exercise_word['French']}", fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- ANSWER MECHANISM ------------------------------- #


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(language_indication, fill="white", text="English")
    canvas.itemconfig(word_translate, fill="white", text=f"{exercise_word['English']}")


# ---------------------------- UI SETUP ------------------------------- #
# Window Config
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
open_dictionary()

flip_timer = window.after(3000, func=flip_card)

# Canvas Config
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Card Flash
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front)

# Text in Card Flash - Canvas
language_indication = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_translate = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons Wrong or Right
wrong_image = PhotoImage(file="./images/wrong.png")
right_image = PhotoImage(file="./images/right.png")

wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong_answer)
wrong_button.grid(column=0, row=1)
right_button = Button(image=right_image, highlightthickness=0, command=right_answer)
right_button.grid(column=1, row=1)

# Start Flash Card
next_card()


window.mainloop()
