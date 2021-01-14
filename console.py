# asks for player two's word to be guessed and returns it
def request_word():
    print ("TODO")

# asks whether or not it is okay to display the word to confirm it was typed correctly and returns yes if it is
def okay_to_confirm():
    print ("TODO")

# asks whether the word shown is correct or not and returns yes if it is correct
def ask_for_confirmation():
    print ("TODO")

# asks for a letter guess and returns it
def ask_for_guess():
    print ("TODO")

# tells the first player (s)he won
def player_one_wins():
    print ("TODO")

# tells the second player (s)he won
def player_two_wins():
    print ("TODO")

# tells the player (s)he lost to the computer
def you_lose() :
    print ("TODO")

# tells the player (s)he defeated the computer
def you_win():
    print ("TODO")

# asks if two or one players will be playing, and returns the boolean answer
def ask_if_multiplayer():
    while True:
        line = input("Enter the number of players (1 or 2):")
        if (line.strip() == "1"):
            return False
        if (line.strip() == "2"):
            return True
        print("You must enter a valid response of \"1\" or \"2\" players.")

# requests the integer number of letters that is the length of the random word and returns it or zero (if length is to be unspecified)
def ask_number_letters():
    while True:
        line = input("Enter the length of the word to guess, or \"any\" if you would like it to be randomized.")
        if (line.strip() == "any"):
            return 0
        try:
            value = int(line)
            if (value > 3):
                return value
            else:
                print("A word with which hangman is to be played must be at least 4 letters long.")
        except ValueError:
            print("Uh oh, you didn't enter an integer or the word \"any\"! Try again.")

# asks if the user wants to play again or if they would like to exit and returns the boolean answer
def play_again():
    while True:
        line = input("Would you like to play again? (yes/no)")
        if (line.strip() == "yes"):
            return True
        if (line.strip() == "no"):
            return False
        print("You must answer with either \"yes\" or \"no\".")

# asks if the player would like to use the same settings as the last game and returns the boolean answer
def change_settings():
    while True:
        line = input("Would you like to change the game settings? (yes/no)")
        if (line.strip() == "yes"):
            return True
        if (line.strip() == "no"):
            return False
        print("You must answer with either \"yes\" or \"no\".")