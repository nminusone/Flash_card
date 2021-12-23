from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
selection = []
# _______________________________________________Read csv to dataframe_________________________________________________
# with open('./data/french_words.csv') as file:
try:
    word_pairs = pd.read_csv("./data/words_to_learn.csv")
    word_list = word_pairs.to_dict('records')
except FileNotFoundError:
    word_pairs = pd.read_csv('./data/french_words.csv')
    word_list = word_pairs.to_dict('records')
    words_to_learn = word_list
    print(word_list)


# ______________________________Get random key:value from list of dictionaries__________________________________________
def random_select():
    global selection
    selection = random.choice(word_list)
    canvas.itemconfig(canvas_image, image=front_img)
    lang_label.config(text='French', bg='white', fg='black')
    word_label.config(text=selection['French'], bg='white', fg='black')
    window.after(3000, func=flip)


def flip():
    global selection
    lang_label.config(text='English', bg=BACKGROUND_COLOR, fg='white')
    word_label.config(text=selection['English'], bg=BACKGROUND_COLOR, fg='white')
    canvas.itemconfig(canvas_image, image=back_img)
    print("It's time")


# ____________________________________________________________GUI Setup________________________________________________

window = Tk()
window.title('Flash Card Game')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file='./images/card_front.png')
back_img = PhotoImage(file='./images/card_back.png')
right_img = PhotoImage(file='./images/right.png')
wrong_img = PhotoImage(file='./images/wrong.png')
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2, rowspan=3)

right_button = Button(image=right_img, highlightthickness=0, command=random_select)
right_button.grid(row=3, column=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=random_select)
wrong_button.grid(row=3, column=0)

lang_label = Label(text='Language', bg='white')
lang_label.config(font=('arial', 40, 'italic'))
lang_label.grid(row=0, column=0, columnspan=2)

word_label = Label(text='Word', bg='white')
word_label.config(font=('arial', 60, 'bold'))
word_label.grid(row=1, column=0, columnspan=2)

random_select()

# TODO Create new flash cards

# TODO Flip the cards

# TODO Save your progress


window.mainloop()
