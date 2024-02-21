import tkinter as tk
from cgitb import text
from unittest import result

window = tk.Tk()
window.title("Doz Game")

global turn, results
turn = "X"
results = ["", "", "", "", "", "", "", "", ""]


def clicked(btn):
    global turn
    btn = int(btn)

    if results[btn] == "":

        if turn == "X":
            results[btn] = "X"
            buttens[btn]["bg"] = "red"
            buttens[btn]["fg"] = "white"
            buttens[btn]["text"] = "X"
            buttens[btn]["relief"]=tk.RIDGE
          #  buttens[btn]["state"]=tk.DISABLED
            turn = "O"

        else:
            results[btn] = "O"
            buttens[btn]["bg"] = "green"
            buttens[btn]["fg"] = "white"
            buttens[btn]["text"] = "O"
        #  buttens[btn]["state"]=tk.DISABLED
            turn = "X"
        print(results)


def point():
    board_frame = tk.Frame(window)
    board_frame.grid(row=0)
    label_player_one = tk.Label(board_frame, text="player num1", padx=10)
    label_player_two = tk.Label(board_frame, text="player num2", padx=10)
    label_player_one.grid(row=0, column=0)
    label_player_two.grid(row=0, column=2)

    point_frame = tk.Frame(window)
    point_frame.grid(row=1)
    point_player_one = tk.Label(point_frame, text="0", padx=20)
    point_player_two = tk.Label(point_frame, text="0", padx=20)
    point_player_one.grid(row=0, column=0)
    point_player_two.grid(row=0, column=1)


def boards():
    global buttens
    buttens = []
    counter = 0
    board_frame = tk.Frame(window)
    board_frame.grid(row=2)
    for row in range(1, 4):
        for colum in range(1, 4):
            index = counter
            buttens.append(index)
            buttens[index] = tk.Button(
                board_frame, command=lambda x=f"{index}": clicked(x))
            buttens[index].config(width=10, height=4,
                                  font=("none", 10, "bold"))
            buttens[index].grid(row=row, column=colum)
            counter += 1


point()
boards()
window.mainloop()
#18:48
