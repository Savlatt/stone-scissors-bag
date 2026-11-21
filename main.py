import tkinter
import random
from tkinter import PhotoImage

def re_boot():
    sten_button.destroy()
    sax_button.destroy()
    pase_button.destroy()

def quit_button():
    quitbutton = tkinter.Button(
        root,
        text=" Quit ",
        font=("Arial", 25, "bold"),
        bg="grey",
        command=lambda: root.destroy(),
        activebackground="white",
        activeforeground="red"
    )
    quitbutton.place(x=240, y=360)

def win_txt():
    UserWin1 = tkinter.Label(
        root,
        text="Du vann",
        font=("Arial", 30, "bold")
    )
    UserWin1.place(x=218, y=10)

def user_lose():
    Botwon = tkinter.Label(
        root,
        text="Bot vann",
        font=("Arial", 30, "bold")
    )
    Botwon.place(x=215, y=10)

def game_rule():

    bot_val = random.choice(["Sax", "Sten", "Påse"])
    print(bot_val)

    if bot_val == user_val:
        tie = tkinter.Label(
            root,
            text="Oavgjord",
            font=("Arial", 30, "bold")
        )
        tie.place(x=209, y=300)

        Mr_bean = tkinter.Label(
            root,
            image=tie_photo
        )
        Mr_bean.place(x=227, y=100)

        quit_button()
        re_boot()

    elif bot_val == "Sax" and user_val == "Sten":
        bot_val_txt = tkinter.Label(
            root,
            image=bot_saxphoto
        )
        bot_val_txt.place(x=227, y=67)

        win_txt()
        quit_button()
        re_boot()

    elif bot_val == "Påse" and user_val == "Sax":
        bot_val_txt = tkinter.Label(
            root,
            image=bot_pasephoto
        )
        bot_val_txt.place(x=227, y=67)

        win_txt()
        quit_button()
        re_boot()

    elif bot_val == "Sten" and user_val == "Påse":
        bot_val_txt = tkinter.Label(
            root,
            image=bot_stenphoto
        )
        bot_val_txt.place(x=227, y=67)

        win_txt()
        quit_button()
        re_boot()

    elif user_val == "Sax" and bot_val == "Sten":
        bot_val_txt = tkinter.Label(
            root,
            image=bot_stenphoto
        )
        bot_val_txt.place(x=227, y=67)

        user_lose()
        quit_button()
        re_boot()

    elif user_val == "Påse" and bot_val == "Sax":
        bot_val_txt = tkinter.Label(
            root,
            image=bot_saxphoto
        )
        bot_val_txt.place(x=227, y=67)

        user_lose()
        quit_button()
        re_boot()

    elif user_val == "Sten" and bot_val == "Påse":
        bot_val_txt = tkinter.Label(
            root,
            image=bot_pasephoto
        )
        bot_val_txt.place(x=227, y=67)

        user_lose()
        quit_button()
        re_boot()

def sax():
    global user_val
    user_val = "Sax"
    game_rule()

def sten():
    global user_val
    user_val = "Sten"
    game_rule()

def pase():
    global user_val
    user_val = "Påse"
    game_rule()


root = tkinter.Tk()

bg_image = (tkinter.PhotoImage(file="S_S_T_bg_image.png"))

background_label = tkinter.Label(
    root,
    image=bg_image
)

background_label.place(x=0, y=0, relwidth=1, relheight=1)

user_saxphoto = PhotoImage(file="bild.user.sax.png")
user_stenphoto = PhotoImage(file="bild.user.sten.png")
user_pasephoto = PhotoImage(file="bild.user.påse.png")
game_icon = PhotoImage(file="Appicon_S_S_T.png")
bot_saxphoto = PhotoImage(file="bild.bot.sax.png")
bot_stenphoto = PhotoImage(file="bild.bot.sten.png")
bot_pasephoto = PhotoImage(file="bild.bot.påse.png")

tie_photo = PhotoImage(file="tie.photo.png")

root.title("Sten, Sax, Påse")

root.config(bg="white")

root.iconphoto(True, game_icon)

root.geometry("600x500")

root.resizable(width=False, height=False)


sten_button = tkinter.Button(
    root,
    image=user_stenphoto,
    font=("Arial", 12, "bold"),
    bg="grey",
    command=sten,
    activebackground="white",
    activeforeground="lime"
)

sten_button.place(x=30, y=250)


sax_button = tkinter.Button(
    root,
    image=user_saxphoto,
    font=("Arial", 12, "bold"),
    bg="grey",
    command=sax,
    activebackground="white",
    activeforeground="lime"
)

sax_button.place(x=220, y=250)


pase_button = tkinter.Button(
    root,
    image=user_pasephoto,
    font=("Arial", 12, "bold"),
    bg="grey",
    command=pase,
    activebackground="white",
    activeforeground="lime"
)

pase_button.place(x=410, y=250)


root.mainloop()
