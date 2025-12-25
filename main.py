from tkinter import *
from game import launch_game
from leaderboard import calculate_points

def start_game(mode, size, window, difficulty=None):
    window.destroy()
    launch_game(mode, size, show_name() ,difficulty)
    pass

def choose_window(gamemode):

    global choice_window

    choice_window = Toplevel(main_window)

    choice_window.geometry("500x200")
    choice_window.title("Choose the board size")

    logo = PhotoImage(file='tictactoe.png')
    choice_window.iconphoto(True, logo)

    choice_window.columnconfigure((0,1,2), weight=1)  # 3 columns expand equally
    choice_window.rowconfigure(0, weight=1) 

    if gamemode == "multi":

        three_button = Button(choice_window, text="3x3", height=5, width=10, command=lambda: start_game("PVP", 3, choice_window))
        three_button.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        four_button = Button(choice_window, text="4x4", height=5, width=10, command=lambda: start_game("PVP", 4, choice_window))
        four_button.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)

        five_button = Button(choice_window, text="5x5", height=5, width=10, command=lambda: start_game("PVP", 5, choice_window))
        five_button.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)

    elif gamemode == "single":
        
        easy_button = Button(choice_window, text="Easy", height=5, width=10, command=lambda: start_game("AI", 3, choice_window, "e"))
        easy_button.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        medium_button = Button(choice_window, text="Medium", height=5, width=10, command=lambda: start_game("AI", 3, choice_window, "m"))
        medium_button.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)

        hard_button = Button(choice_window, text="Hard", height=5, width=10, command=lambda: start_game("AI", 3, choice_window, "h"))
        hard_button.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)
        
    pass

def show_name():

    global name

    name = name_entry.get()
    if name != "":
        name_label.config(text=f"Welcome, {name}")
        
    return name


main_window = Tk()          

main_window.geometry("550x200")
main_window.title("TicTacToe")

logo = PhotoImage(file='tictactoe.png')
main_window.iconphoto(True, logo)

multiplayer_button = Button(main_window, text="Multiplayer", height=2, width=30, command=lambda: choose_window("multi"))
singleplayer_button = Button(main_window, text="Singleplayer", height=2, width=30, command= lambda:choose_window("single"))

multiplayer_button.place(relx=0.5, rely=0.37, anchor=CENTER)

singleplayer_button.place(relx=0.5, rely=0.63, anchor=CENTER)

name_entry = Entry(main_window)
name_entry.place(relx=0.4, rely=0.15, anchor=CENTER)

submit_button = Button(main_window, text="Submit", command=show_name, height = 1, width = 8)
submit_button.place(relx=0.67, rely=0.15, anchor=CENTER)

name_label = Label(main_window)
name_label.place(relx=0.5, rely=0.87, anchor=CENTER)

leaderboard_frame = Frame(main_window)
leaderboard_frame.columnconfigure((0,1,2), weight=1) 
#leaderboard_frame.place(relx=0.89, rely = 0.2, anchor=CENTER)
leaderboard_frame.pack(side=RIGHT)

rank_header = Label(leaderboard_frame, text="Rank")
rank_header.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
name_header = Label(leaderboard_frame, text="Name")
name_header.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
points_header = Label(leaderboard_frame, text="Points")
points_header.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)

results = calculate_points("e")

for i, data in enumerate(results):

    rank_label = Label(leaderboard_frame, text=str(i+1))
    name_label = Label(leaderboard_frame, text=data[0])
    points_label = Label(leaderboard_frame, text=data[1])

    rank_label.grid(row=i+1, column=0, sticky="nsew", padx=2, pady=2)
    name_label.grid(row=i+1, column=1, sticky="nsew", padx=2, pady=2)
    points_label.grid(row=i+1, column=2, sticky="nsew", padx=2, pady=2)

    if i == 5:
        break




main_window.mainloop()
