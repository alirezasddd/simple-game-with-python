import tkinter as tk

window = tk.Tk()
window.title("Doz Game")


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
    point_player_two.grid(row=0,column=1)



def boards():
    buttens = []
    conter = 0 
    board_frame = tk.Frame(window)
    board_frame.grid(row=2)

point()
window.mainloop()
