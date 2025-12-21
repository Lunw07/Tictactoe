from tkinter import *
from game import launch_game
main_window = Tk()          

main_window.geometry("500x200")
main_window.title("TicTacToe")

logo = PhotoImage(file='tictactoe.png')
main_window.iconphoto(True, logo)


multiplayer_button = Button(main_window, text="Multiplayer", height=2, width=30, command=lambda: launch_game("PVP"))
singleplayer_button = Button(main_window, text="Singleplayer", height=2, width=30)

multiplayer_button.place(relx=0.5, rely=0.37, anchor=CENTER)


singleplayer_button.place(relx=0.5, rely=0.63, anchor=CENTER)




main_window.mainloop()
