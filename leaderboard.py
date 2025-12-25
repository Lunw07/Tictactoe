from tkinter import *
import json

game_scores = {
    "name": "",
    "x": 0,             # losses
    "o": 2,             # wins
    "draws": 0
}

def add_name(name):
    game_scores["name"] = name

def add_win(player):
    game_scores[player] += 1
    pass

def add_draw():
    game_scores["draws"] += 1
    
def get_scores():
    return game_scores.copy

def save_scores(gamemode):                  # when someone wins

    found = False

    with open("data.json", "r") as f:
        data = json.load(f)
    
    for entry in data[gamemode]["leaderboard"]:
        if entry["name"].strip().lower() == game_scores["name"].strip().lower():
            entry["x"] = game_scores["x"]
            entry["o"] = game_scores["o"]
            entry["draws"] = game_scores["draws"]
            found = True

    if not found:
        data[gamemode]["leaderboard"].append(game_scores)

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    pass

def calculate_points(gamemode):             # find points depending on no. of wins and losses

    # win = 3, draw = 0, loss = -2

    name_points = {}

    with open("data.json", "r") as f:
        data = json.load(f)
    
    for entry in data[gamemode]["leaderboard"]:
        points = entry["o"] * 3 - entry["x"] * 2
        name_points[entry["name"]] = points

    sorted_list = sorted(name_points.items(), key = lambda item:item[0])

    return sorted_list

    pass

def display_points():
    
    pass

def reset_scores():
    game_scores["name"] = ""
    game_scores["x"] = 0
    game_scores["o"] = 0
    game_scores["draws"] = 0
    
calculate_points("e")
