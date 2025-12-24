from tkinter import *
import random
import time

game_mode = "PVP"    
human_player = "o"
ai_player = "x"
ai_difficulty = "e"                 # e = easy, m = medium, h = hard

def next_turn(row, column):

    global player
    global turn_label

    if buttons[row][column]["text"] == "":
        make_move(row, column, player)

        switch_player()
        change_label(player)
        check_windraw()

        player_won, cells = winner()

        if player_won is not None:              # prevents AI from moving after player wins
            return

        if game_mode == "AI" and player == ai_player:           
            disable_all_buttons()
            window.after(500, ai_turn)

def make_move(row, col, p):         # p is player
    buttons[row][col]["text"] = p
    buttons[row][col]["state"] = DISABLED
    results[row][col] = p

def switch_player():
    global player

    if player == players[0]:        # if player = "x"
        player = players[1]
    else:
        player = players[0]

def change_label(current_player):
    if game_mode == "PVP":
        turn_label.config(text = player + "' s Turn", fg = players_colour[current_player])
    else:
        if current_player == human_player:
            turn_label.config(text = "Your Turn", fg = players_colour[current_player])
        else:
            turn_label.config(text = "AI's Turn", fg = players_colour[current_player])

def check_windraw():

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
                for row in range(len(results)):
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

    # for row in range(len(results)):
    #     for column in range(len(results[0])):
    #         if results[row][column] == "":
    #             return False                    # if any empty spaces then its a draw

    if any_empty():
        return False
            
    player_won, cells = winner()

    if player_won is None:                          # if winner == None and board is full then draw
        return True         
    else:
        return False

    pass

def any_empty():                # True if there is any row with "" in it
    return any("" in row for row in results)

def disable_all_buttons():
    for row in buttons:
        for button in row:
            button["state"] = DISABLED

def enable_empty_buttons():
    player_won, cells = winner()

    if player_won is not None:              # prevents AI from moving after player wins
        return

    for row in buttons:
        for button in row:
            if button["text"] == "":
                button["state"] = NORMAL
            else:
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

    if game_mode == "AI" and player == ai_player:
        easy_ai()

    turn_label.config(text = player + "' s Turn", fg = players_colour[player])

def ai_turn():
    if ai_difficulty == "e":
        easy_ai()
    elif ai_difficulty == "m":
        medium_ai()
    elif ai_difficulty == "h":
        hard_ai()
        pass
    else:
        print("Wrong AI difficulty")
        return
    enable_empty_buttons()
   
def easy_ai():

    # if ai turn, select random square (disable button too)
    # if square already filled in then repeat
    global player

    random_row = random.randint(0, len(results)-1)
    random_col = random.randint(0, len(results[0])-1)

    while results[random_row][random_col] != "" and any_empty():
        random_row = random.randint(0, len(results)-1)
        random_col = random.randint(0, len(results[0])-1)
    
    make_move(random_row, random_col, player)

    switch_player()
    change_label(player)
    check_windraw()
    
    pass

def medium_ai():
    pass

def hard_ai():
    global player
    move = find_best_move()
    print(move)

    if move is None:
        return

    make_move(move[0], move[1], player)

    switch_player()
    change_label(player)
    check_windraw()

    pass

def find_best_move():

    global results

    best_score = -float("inf")
    best_move = None

    for row in range(len(results)):
        for column in range(len(results[0])):
            if results[row][column] == "":
                results[row][column] = ai_player
                score = minimax(0, False)
                results[row][column] = ""
                if score > best_score:
                    best_score = score
                    best_move = (row, column)
    return best_move
    pass

def minimax(depth, is_maximising):

    global results


    if winner()[0] == ai_player:
        return 1
    elif winner()[0] == human_player:
        return -1
    elif draw():
        return 0
    
    if is_maximising:
        best_score = -float("inf")
        for row in range(len(results)):
            for column in range(len(results[0])):
                if results[row][column] == "":
                    results[row][column] = ai_player
                    score = minimax(depth+1, False)
                    results[row][column] = ""
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for row in range(len(results)):
            for column in range(len(results[0])):
                if results[row][column] == "":
                    results[row][column] = human_player
                    score = minimax(depth+1, True)
                    results[row][column] = ""
                    best_score = min(best_score, score)
        return best_score


    pass

def launch_game(mode, size, difficulty=None):

    global window, buttons, results, player, turn_label, players, players_colour, game_mode, frame, ai_difficulty

    game_mode = mode
    ai_difficulty = difficulty

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
    
    buttons = [ [0]* (size) for i in range(size)]
    results = [ [""]* (size) for i in range(size)]


    if mode == "PVP": 
        turn_label = Label(window, text = player + "' s Turn", font = ("Arial", 15), fg = players_colour[player])
    else:
        if player == human_player: 
            turn_label = Label(window, text = "Your Turn", font = ("Arial", 15), fg = players_colour[player])
        else:
            turn_label = Label(window, text = "AI' s Turn", font = ("Arial", 15), fg = players_colour[player])

    turn_label.pack()

    button_frame = Frame(window)
    button_frame.pack(side=BOTTOM)

    reset_button = Button(window, text = "Reset", bg = "red", font = ("Arial", 20), command = reset_game)
    reset_button.pack(side=BOTTOM,padx=5, pady= 5)
    
    frame = Frame(window, width = 600, height = 600)
    frame.pack(expand = True, fill = BOTH)

    for row in range(len(buttons)):
        frame.rowconfigure(row, weight=1)      # makes all rows same height
        frame.columnconfigure(row, weight=1)
        for column in range(len(buttons[0])):
            buttons[row][column] = Button(frame, text="",font=('Arial',40), width=5, height=3,
                                        command= lambda row=row, column=column: next_turn(row,column))
            buttons[row][column].grid(row=row, column=column, sticky="nsew")

    if game_mode == "AI" and player == ai_player:
        easy_ai()

    window.mainloop()



