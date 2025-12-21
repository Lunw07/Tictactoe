from tkinter import *
from game import launch_game

def start_game(mode, size, window):
    window.destroy()

    launch_game(mode, size)
    pass

def multiplayer_choice():

    global choice_window

    choice_window = Toplevel(main_window)

    choice_window.geometry("500x200")
    choice_window.title("Choose the board size")

    logo = PhotoImage(file='tictactoe.png')
    choice_window.iconphoto(True, logo)

    choice_window.columnconfigure((0,1,2), weight=1)  # 3 columns expand equally
    choice_window.rowconfigure(0, weight=1) 

    three_button = Button(choice_window, text="3x3", height=5, width=10, command=lambda: start_game("PVP", 3, choice_window))
    three_button.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    four_button = Button(choice_window, text="4x4", height=5, width=10, command=lambda: start_game("PVP", 4, choice_window))
    four_button.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)

    five_button = Button(choice_window, text="5x5", height=5, width=10, command=lambda: start_game("PVP", 5, choice_window))
    five_button.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)


    pass

main_window = Tk()          

main_window.geometry("500x200")
main_window.title("TicTacToe")

logo = PhotoImage(file='tictactoe.png')
main_window.iconphoto(True, logo)


multiplayer_button = Button(main_window, text="Multiplayer", height=2, width=30, command=lambda: multiplayer_choice())
singleplayer_button = Button(main_window, text="Singleplayer", height=2, width=30)

multiplayer_button.place(relx=0.5, rely=0.37, anchor=CENTER)

singleplayer_button.place(relx=0.5, rely=0.63, anchor=CENTER)

main_window.mainloop()
