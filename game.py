from tkinter import *
import random

def next_turn(row, column):

    global player
    global turn_label

    if buttons[row][column]["text"] == "":
        buttons[row][column]["text"] = player
        buttons[row][column]["state"] = DISABLED

        results[row][column] = player

        if player == players[0]:
            player = players[1]
        else:
            player = players[0]

        turn_label.config(text = player + "' s Turn", fg = players_colour[player])

    #print(winner())

    player_won, cells = winner()

    if player_won is not None:
        turn_label.config(text = player_won + " has Won!", font = ("Arial, 20"), fg = "green")
        disable_all_buttons()

        for row, col in cells:
            buttons[row][col]["bg"] = "#5CE65C"

    if draw():
        turn_label.config(text = "DRAW", font = ("Arial", 20), fg = "yellow")
        disable_all_buttons()

    pass

def winner():


    for row in range(len(results)):         # check rows (horizontal)
        winner = results[row][0]             # Using the first element of the row, check if the entire row is the same
        if winner != "":
            row_win = True                  # Initially set as True as if its wrong, it will set it as false anyways
            for x in results[row]:
                if x != winner:
                    row_win = False
                    break
            if row_win:    
                winning_cells = []
                for col in range(len(results[row])):
                    winning_cells.append((row, col))

                return (winner, winning_cells)
        
    for column in range(len(results[0])):
        winner = results[0][column]             
        if winner != "":
            col_win = True
            for row in range(len(results)):
                if results[row][column] != winner:
                    col_win = False
                    break
            if col_win:      

                winning_cells = []
                for row in range(len(results[row])):
                    winning_cells.append((row, column))

                return (winner, winning_cells)

    # Diagonals (Top left to bottom right)

    winner = results[0][0]
    if winner != "":
        dia_win =  True
        for i in range(len(results)):
            if results[i][i] != winner:
                dia_win = False
                break

        if dia_win:
            winning_cells = []
            for i in range(len(results)):
                winning_cells.append((i, i))

            return (winner, winning_cells)
    # Diagonals (Top right to bottom left)

    winner = results[0][2]
    if winner != "":
        dia_win =  True
        x = len(results[0]) - 1

        for i in range(len(results)):
            if results[i][x] != winner:
                dia_win = False
                break
            x -= 1

        if dia_win:
            winning_cells = []
            x = len(results[0]) - 1

            for i in range(len(results)):
                winning_cells.append((i, x))
                x -= 1

            return (winner, winning_cells)
        
    return (None, [])

    pass

def draw():

    for row in range(len(results)):
        for column in range(len(results[0])):
            if results[row][column] == "":
                return False                    # if any empty spaces then its a draw
            
    player_won, cells = winner()


    if player_won is None:                          # if winner == None and board is full then draw
        return True         
    else:
        return False

    pass

def disable_all_buttons():
    for row in buttons:
        for button in row:
            button["state"] = DISABLED

def reset_game():

    global player

    for row in range(len(buttons)):
        for column in range(len(buttons[0])):
            buttons[row][column].config(text = "")
            results[row][column] = ""
            buttons[row][column]["state"] = NORMAL
            buttons[row][column]["bg"] = "lightgray"


    
    player = random.choice(players)
    turn_label.config(text = player + "' s Turn", fg = players_colour[player])


def launch_game(mode, size):

    global window, buttons, results, player, turn_label, players, players_colour


    window = Toplevel()         

    window.geometry("600x700")
    window.title("TicTacToe")

    players = ["x", "o"]
    player = random.choice(players)

    players_colour = {players[0]: "red",
                    players[1]: "blue"}

    logo = PhotoImage(file='tictactoe.png')
    window.iconphoto(True, logo)
    window.config(background="lightgray")
        

    # buttons = [[0,0,0,0],
    #         [0,0,0,0],
    #         [0,0,0,0],
    #         [0,0,0,0]]

    # results = [["","","",""],
    #         ["","","",""],
    #         ["","","",""],
    #         ["","","",""]]
    
    buttons = [ [0]* (size) for i in range(size)]
    results = [ [""]* (size) for i in range(size)]


    turn_label = Label(window, text = player + "' s Turn", font = ("Arial", 15), fg = players_colour[player])
    turn_label.pack()

    frame = Frame(window, width = 600, height = 600)
    frame.pack(expand = True, fill = BOTH)

    for row in range(len(buttons)):
        frame.rowconfigure(row, weight=1)      # makes all rows same height
        frame.columnconfigure(row, weight=1)
        for column in range(len(buttons[0])):
            buttons[row][column] = Button(frame, text="",font=('Arial',40), width=5, height=3,
                                        command= lambda row=row, column=column: next_turn(row,column))
            buttons[row][column].grid(row=row, column=column, sticky="nsew")



    reset_button = Button(window, text = "Reset", bg = "red", font = ("Arial", 20), command = reset_game)
    reset_button.pack(side=BOTTOM)
    window.mainloop()

