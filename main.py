import tkinter as tk
import random

# Define the choices
choices = ["Rock", "Paper", "Scissors"]


# Determine the winner
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Scissors" and computer_choice == "Paper") or
            (user_choice == "Paper" and computer_choice == "Rock")
    ):
        return "You win!"
    else:
        return "You lose!"


# Function to play the game
def play_game(user_choice):
    computer_choice = random.choice(choices)
    result = get_winner(user_choice, computer_choice)

    # Update the labels with the choices and result
    user_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)


# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Add labels
title_label = tk.Label(root, text="Rock, Paper, Scissors Game", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

user_choice_label = tk.Label(root, text="You chose: ", font=("Arial", 12))
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12))
computer_choice_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Add buttons for choices
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, font=("Arial", 12), command=lambda: play_game("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, font=("Arial", 12), command=lambda: play_game("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, font=("Arial", 12),
                            command=lambda: play_game("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Add a quit button
quit_button = tk.Button(root, text="Quit", width=10, font=("Arial", 12), command=root.destroy)
quit_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
