from tkinter import *
import random

def next_turn(row, column):

    global player
    global turn_label

    if buttons[row][column]["text"] == "":
        buttons[row][column]["text"] = player
        buttons[row][column]["font"] = ("Arial", 40, "bold")  # bigger font

        buttons[row][column]["state"] = DISABLED

        if player == players[0]:
            player = players[1]
        else:
            player = players[0]

        turn_label.config(text = player + "' s Turn", fg = players_colour[player])

    pass

def winner():

    pass


window = Tk()          # instantiates an instance of window 

window.geometry("600x700")
window.title("TicTacToe")

players = ["x", "o"]
player = random.choice(players)

players_colour = {players[0]: "red",
                  players[1]: "blue"}

logo = PhotoImage(file='tictactoe.png')
window.iconphoto(True, logo)
window.config(background="lightgray")

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

results = [["","",""],
           ["","",""],
           ["","",""]]

turn_label = Label(window, text = player + "' s Turn", font = ("Arial", 15), fg = players_colour[player])
turn_label.pack()

frame = Frame(window)
frame.pack()

for row in range(len(buttons)):
    for column in range(len(buttons[0])):
        buttons[row][column] = Button(frame, text="",font=('Arial',40), width=5, height=3,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()

