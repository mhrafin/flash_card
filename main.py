import tkinter as tk
from random import randint

import pandas as pd

from text_to_png import to_png

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 40, "bold")
FONT_WORD = ("Arial", 60)
FONT_PARTSOFSPEECH = ("Arial", 20)


def get_ar_word():
    """Reads the learned_words.txt to make learned words list of str with ids. If the current word is found in the learned words it will choose a different word.
    If the word is not in the learned words list and the length of the learned words are lower than total records then display new arabic word and start the timer.
    """
    global curr_record
    global curr_ar_image
    global flip_timer

    try:
        with open("data/learned_words.txt", mode="r") as learned_file:
            learned_words = [
                line.replace("\n", "") for line in learned_file.readlines()
            ]
    except FileNotFoundError:
        with open("data/learned_words.txt", mode="w") as learned_file:
            learned_words = []
            pass

    # print(learned_words)
    curr_record = randint(0, total_records)

    found_curr_word = True

    while found_curr_word:
        found_curr_word = False
        for word in learned_words:
            # print(f"get ar {type(word)} = {type(id_data[curr_record])}")
            # print(f"get ar {(word)} = {(id_data[curr_record])}")

            if word == str(id_data[curr_record]):
                curr_record = randint(0, total_records)
                found_curr_word = True
            # print(f"{found_curr_word=}")
            # print()

        # print(total_records)
        if total_records < len(learned_words):
            curr_ar_image = to_png(text=" ", color=(0, 0, 0))
            canvas.itemconfig(
                language_canvas, text="You Learned All Words!", fill="black"
            )
            canvas.itemconfig(pos_canvas, text="", fill="black")
            reset = tk.Button(
                text="Reset",
                command=reset_learned,
                relief="flat",
                background=BACKGROUND_COLOR,
                activebackground=BACKGROUND_COLOR,
                highlightthickness=0,
            )
            reset.grid(column=1, row=2)
            window.after_cancel(flip_timer)
            return

    window.after_cancel(flip_timer)

    canvas.itemconfig(language_canvas, text=arabic_words.name, fill="black")
    curr_ar_image = to_png(text=arabic_words[curr_record], color=(0, 0, 0))
    canvas.itemconfig(word_canvas, image=curr_ar_image)
    canvas.itemconfig(pos_canvas, text=word_is_a[curr_record], fill="black")
    canvas.itemconfig(card_canvas, image=card_q)

    flip_timer = window.after(6000, flip_card)


def not_knew_it():
    """Cancels the timer. Appends the current word to need_to_learn.txt. If the file does not exists, creates it. Calls get_ar_word()."""
    global flip_timer
    window.after_cancel(flip_timer)
    try:
        with open("data/need_to_learn.txt", mode="a") as data_file:
            data_file.write(
                f"{arabic_words[curr_record]},{english_words[curr_record]}\n"
            )
    except FileNotFoundError:
        with open("data/need_to_learn.txt", mode="w") as data_file:
            data_file.writelines(
                [
                    "Arabic,English",
                    f"{arabic_words[curr_record]},{english_words[curr_record]}\n",
                ]
            )
    get_ar_word()


def flip_card():
    """Gets the english meaning of the current arabic word and displays it."""

    global curr_ar_image

    canvas.itemconfig(language_canvas, text=english_words.name, fill="white")

    curr_ar_image = to_png(text=english_words[curr_record], color=(255, 255, 255))
    canvas.itemconfig(word_canvas, image=curr_ar_image)
    canvas.itemconfig(pos_canvas, text=word_is_a[curr_record], fill="white")
    canvas.itemconfig(card_canvas, image=card_a)


def knew_it():
    """Searches for the current word in the learned word. If its there then breaks and calls get_ar_word(). Else appends the new word to learned_words.txt."""
    try:
        with open("data/learned_words.txt", mode="r") as data_file:
            found_learned_word = False
            for line in data_file.readlines():
                # print(f"knew it {line} = {id_data[curr_record]}")
                if str(id_data[curr_record]) == line.replace("\n", ""):
                    found_learned_word = True
                    break
            if found_learned_word is False:
                # print("writing")
                with open("data/learned_words.txt", mode="a") as data_file:
                    data_file.write(f"{id_data[curr_record]}\n")
    except FileNotFoundError:
        with open("data/learned_words.txt", mode="w") as data_file:
            data_file.write(
                f"{arabic_words[curr_record]}\n",
            )
    get_ar_word()


def reset_learned():
    """Clears all the data in learned_words.txt and need_to_learn.txt. Starts the timer and calls get_ar_word()"""
    global flip_timer
    with open("data/learned_words.txt", mode="w"):
        pass
    with open("data/need_to_learn.txt", mode="w"):
        pass

    flip_timer = window.after(3000, flip_card)
    get_ar_word()


with open("data/need_to_learn.txt", mode="w"):
    pass

# TODO UI setup
window = tk.Tk()
window.title("Learn Words From The Quran")
window.config(padx=40, pady=40, background=BACKGROUND_COLOR)

card_q = tk.PhotoImage(file="images/card_front.png")
card_a = tk.PhotoImage(file="images/card_back.png")


canvas = tk.Canvas(
    width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0
)
card_canvas = canvas.create_image(400, 263, image=card_q)

language_canvas = canvas.create_text(400, 150, text="Language", font=FONT_TITLE)
word_canvas = canvas.create_image(400, 263)  # Placeholder
pos_canvas = canvas.create_text(
    400, 313, text="(Ready To Learn!)", font=FONT_PARTSOFSPEECH
)
canvas.grid(column=0, row=0, columnspan=3)

correct_img = tk.PhotoImage(file="images/right.png")
wrong_img = tk.PhotoImage(file="images/wrong.png")

correct_btn = tk.Button(
    image=correct_img,
    bd=0,
    relief="flat",
    background=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR,
    highlightthickness=0,
    pady=20,
    command=knew_it,
)
correct_btn.grid(column=0, row=1)

wrong_btn = tk.Button(
    image=wrong_img,
    bd=0,
    relief="flat",
    background=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR,
    highlightthickness=0,
    pady=20,
    command=not_knew_it,
)
wrong_btn.grid(column=2, row=1)

text = tk.Label(
    text="Did you get it?", font=("Arial", 20, "bold"), background=BACKGROUND_COLOR
)
text.grid(column=1, row=1)

# Data
data = pd.read_csv("data/arabic_words.csv")
arabic_words = data.Arabic
english_words = data.English
word_is_a = data["Is a _"]
id_data = data.ID

total_records = len(data) - 1

flip_timer = window.after(3000, flip_card)
get_ar_word()

# print(len(arabic_words))
# print(english_words)
# print(word_is_a)


window.mainloop()
