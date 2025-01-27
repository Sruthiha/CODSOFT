import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "🤝 It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "🎉 You win!"
    else:
        return "😢 You lose!"

def play_game(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"You chose: {user_choice} {get_emoji(user_choice)}\n"
                             f"Computer chose: {computer_choice} {get_emoji(computer_choice)}\n"
                             f"{result}")
    if result == "🎉 You win!":
        global user_score
        user_score += 1
    elif result == "😢 You lose!":
        global computer_score
        computer_score += 1
    
    score_label.config(text=f"Score - You: {user_score} 🥇, Computer: {computer_score} 🥈")
    play_again_button.pack(pady=20)

def get_emoji(choice):
    if choice == 'rock':
        return '✊'
    elif choice == 'paper':
        return '📝'
    elif choice == 'scissors':
        return '✂️'
    return ''

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text=f"Score - You: {user_score} 🥇, Computer: {computer_score} 🥈")
    result_label.config(text="")
    play_again_button.pack_forget()  

root = tk.Tk()
root.title("Rock, Paper, Scissors Game! 🎮")
root.geometry("500x500")  
root.configure(bg="#ADD8E6")  

user_score = 0
computer_score = 0

title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 28, "bold"), bg="#ADD8E6", fg="#333")
title_label.pack(pady=20)

button_style = {
    'font': ("Helvetica", 16),
    'bg': "#4CAF50",  
    'fg': "white",    
    'activebackground': "#45a049",  
    'width': 12,
    'height': 2
}

rock_button = tk.Button(root, text="Rock ✊", command=lambda: play_game('rock'), **button_style)
paper_button = tk.Button(root, text="Paper 📝", command=lambda: play_game('paper'), **button_style)
scissors_button = tk.Button(root, text="Scissors ✂️", command=lambda: play_game('scissors'), **button_style)

result_label = tk.Label(root, text="", font=("Helvetica", 16), bg="#ADD8E6", fg="#333")
score_label = tk.Label(root, text=f"Score - You: {user_score} 🥇, Computer: {computer_score} 🥈", font=("Helvetica", 16), bg="#ADD8E6", fg="#333")
play_again_button = tk.Button(root, text="Play Again", command=reset_game, font=("Helvetica", 16), bg="#FF5733", fg="white")

rock_button.pack(pady=10)
paper_button.pack(pady=10)
scissors_button.pack(pady=10)
result_label.pack(pady=20)
score_label.pack(pady=10)

root.mainloop()
