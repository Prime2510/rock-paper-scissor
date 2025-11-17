"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays  against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types “quit”.
"""
import random
import tkinter as tk
from tkinter import messagebox

class RPSGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")
        master.resizable(False, False)
        master.configure(bg="#f7cac9")  # Set window background color

        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0  # Track number of ties

        self.label = tk.Label(
            master,
            text="Choose Rock, Paper, or Scissors:",
            font=("Arial", 14),
            bg="#f7cac9",
            fg="#034f84"
        )
        self.label.pack(pady=10)

        self.button_frame = tk.Frame(master, bg="#f7cac9")
        self.button_frame.pack()

        self.rock_button = tk.Button(
            self.button_frame,
            text="Rock",
            width=10,
            command=lambda: self.play_round("rock"),
            bg="#92a8d1",
            fg="white",
            activebackground="#034f84",
            activeforeground="white"
        )
        self.rock_button.grid(row=0, column=0, padx=5)
        self.paper_button = tk.Button(
            self.button_frame,
            text="Paper",
            width=10,
            command=lambda: self.play_round("paper"),
            bg="#b5ead7",
            fg="#034f84",
            activebackground="#59c3c3",
            activeforeground="white"
        )
        self.paper_button.grid(row=0, column=1, padx=5)
        self.scissors_button = tk.Button(
            self.button_frame,
            text="Scissors",
            width=10,
            command=lambda: self.play_round("scissors"),
            bg="#ffb347",
            fg="#034f84",
            activebackground="#ff6961",
            activeforeground="white"
        )
        self.scissors_button.grid(row=0, column=2, padx=5)

        self.result_label = tk.Label(
            master,
            text="",
            font=("Arial", 12),
            bg="#f7cac9",
            fg="#034f84"
        )
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(
            master,
            text="Score - You: 0, Computer: 0, Ties: 0",
            font=("Arial", 12, "bold"),
            bg="#f7cac9",
            fg="#034f84"
        )
        self.score_label.pack(pady=5)

        self.quit_button = tk.Button(
            master,
            text="Quit",
            command=master.quit,
            bg="#ff6961",
            fg="white",
            activebackground="#034f84",
            activeforeground="white"
        )
        self.quit_button.pack(pady=5)

    def play_round(self, player_choice):
        computer_choice = random.choice(self.choices)
        result = ""
        if player_choice == computer_choice:
            result = f"Both chose {player_choice}. It's a tie!"
            self.ties += 1
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            result = f"You chose {player_choice}, computer chose {computer_choice}. You win!"
            self.player_score += 1
        else:
            result = f"You chose {player_choice}, computer chose {computer_choice}. You lose!"
            self.computer_score += 1
        self.result_label.config(text=result)
        self.score_label.config(
            text=f"Score - You: {self.player_score}, Computer: {self.computer_score}, Ties: {self.ties}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()