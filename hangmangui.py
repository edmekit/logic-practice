import random, tkinter as tk

err = 0
progress = []
word = ""
guessed = set()
hangman = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

#funcs
def start_game():
    global err, progress, word, guessed
    err = 0
    guessed = set()
    words = [
    "python", "banana", "window", "guitar", "planet",
    "orange", "rocket", "flower", "castle", "jungle",
    "pencil", "rabbit", "cloud", "bridge", "forest",
    "dragon", "camera", "pirate", "wizard", "island"]
    word = random.choice(words)
    progress = ["_" for i in range(len(word))]
    man.config(text=f"{hangman[err]}\n {" ".join(progress)}")

def guesser():
    global err, progress,word, guessed
    guessers = enter_guess.get().lower()
    enter_guess.delete(0,tk.END)   
    if len(guessers) != 1:
        if guessers == word:
            man.config(text=f"{hangman[err]}\n {" ".join(progress)}\n You win!")
        else:
            err += 1
            man.config(text=f"{hangman[err]}\n {" ".join(progress)}")
    if err == 7:
        man.config(text=f"{hangman[err]}\n {" ".join(progress)}\n You lose!")
    else:
        if guessers in guessed:
            man.config(text=f"{hangman[err]}\n {" ".join(progress)}\n You already guessed that letter. Try again.")
        elif guessers in word:
            for i in range(len(word)):
                if word[i] == guessers:
                    progress[i] = guessers
            man.config(text=f"{hangman[err]}\n {" ".join(progress)}\n Correct guess.")
            if "_" not in progress:
                man.config(text=f"{hangman[err]}\n {" ".join(progress)}\n You win!")
        else:
            err += 1
            man.config(text=f"{hangman[err]}\n {" ".join(progress)}\n Incorrect guess. Try again.")
    guessed.add(guessers)





window = tk.Tk()
window.title("Hangman")
window.geometry("800x600")
start = tk.Button(window, text="Start game", width=10, command=start_game)
start.grid(row=0, column=0, padx=5, pady=5)
man = tk.Label(window, text="hey", width=20, height=10)
man.grid(row=1, column=0, padx=5, pady=5,columnspan=2)
enter_guess = tk.Entry(window, width=5)
enter_guess.grid(row=2, column=0, padx=5, pady=5)
guess = tk.Button(window, text="guess", width=5, command=guesser)
guess.grid(row=2, column=1, padx=5, pady=5)




window.mainloop()