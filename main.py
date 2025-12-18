from tkinter import *
import random

def next_turn(row, column):
    pass








window = Tk()          # instantiates an instance of window 

window.geometry("500x550")
window.title("TicTacToe")

players = ["x", "o"]
player = random.choice(players)

logo = PhotoImage(file='tictactoe.png')
window.iconphoto(True, logo)
window.config(background="lightgray")

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(window, text = player + "' s Turn", font = ("Arial", 15))
label.pack()

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text = "", width = 16, height = 8, 
                                      command = lambda row=row, column = column: next_turn(row,column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()

