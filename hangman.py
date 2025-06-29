import random

err = 0
guessed = set()
print("H A N G M A N")
print("-------------")
print("Choose a category from the ff: Food, Sport, Animal, Country")

hangman_stages = {
    0: """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    1: """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    2: """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    3: """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    4: """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    5: """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    6: """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
}

choice = input().capitalize()

if choice == "Food":
    words = ["apple", "banana", "cherry", "strawberry", "hamburger"]
elif choice == "Sport":
    words = ["basketball", "tennis", "volleyball", "golf", "baseball"]
elif choice == "Animal":
    words = ["dog", "cat", "elephant", "lion", "tiger", "monkey"]
elif choice == "Country":    
    words = ["germany", "france", "italy", "spain", "japan"] 
else:
    while choice not in ["Food", "Sport", "Animal", "Country"]:
        print("Invalid input. Please try again.")
        choice = input().capitalize()
        if choice == "Food":
            words = ["apple", "banana", "cherry", "date", "elderberry"]
        elif choice == "Sport":
            words = ["basketball", "tennis", "volleyball", "golf", "baseball"]
        elif choice == "Animal":
            words = ["dog", "cat", "elephant", "lion", "tiger"]
        elif choice == "Country":    
            words = ["germany", "france", "italy", "spain", "japan"] 

word = random.choice(words)
progress = ["_" for i in range(len(word))]

print("Guess the word:", end = " ")
print(" ".join(progress))
print()
print(hangman_stages[0])
print()


while err <  6:
    guess = input().lower()
    if len(guess) != 1:
        if guess == word:
            print("You win!")
            break
        else:
            err += 1
            print("Incorrect word. Try again.")
            print(" ".join(progress))
            print()
            print(hangman_stages[err])
            print()
    else:
        if guess in guessed:
            print("You already guessed that letter. Try again.")
            print(" ".join(progress))
            print()
            print(hangman_stages[err])
            print()
        elif guess in word:
            print("Correct guess")
            print()
            for i in range(len(word)):
                if word[i] == guess:
                    progress[i] = guess                   
            print(" ".join(progress))   
            if "_" not in progress:
                print("You win!")
                break    
            print()        
        
        else:
            err += 1
            print("Incorrect guess")
            print(" ".join(progress))
            print()
            print(hangman_stages[err])
            print()
        guessed.add(guess)

else:
    print("You lose! The word was:", word)