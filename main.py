from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- HANDLE DATA ------------------------------- #
words = pandas.read_csv("./data/french_words.csv")
words_translation = words.to_dict(orient="records")


def next_card():
    exercise_word = random.choice(words_translation)

    canvas.itemconfig(language_indication, text="French")
    canvas.itemconfig(word_translate, text=f"{exercise_word['French']}")


# ---------------------------- UI SETUP ------------------------------- #
# Window Config
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas Config
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Front Card - Background Canvas - Card Flash
card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front)

# Back Card - Background Canvas - Card Flash
# card_back = PhotoImage(file="./images/card_back.png")
# canvas.create_image(400, 263, image=card_back)

# Text in Card Flash - Canvas
language_indication = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_translate = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons Wrong or Right
wrong_image = PhotoImage(file="./images/wrong.png")
right_image = PhotoImage(file="./images/right.png")

wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

# Start Flash Card
next_card()

window.mainloop()
