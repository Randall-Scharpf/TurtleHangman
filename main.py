from console import request_word, ask_for_confirmation, ask_for_guess, player_one_wins, player_two_wins, you_lose, you_win
from console import ask_if_multiplayer, ask_number_letters, play_again, change_settings
from graphics import display_word, wipe_shown_word, setup_game, draw_body_part, add_to_red_list, fill_in_letter_at, draw_hanger
from list_reader import pick_random_word

# find a word that the player will guess
def get_word(is_multiplayer, length):
    if (is_multiplayer):
        while True:
            word = request_word()
            display_word(word)
            if(ask_for_confirmation()):
                wipe_shown_word()
                break
            wipe_shown_word()
    else:
        while (length > 0 and len(word) != length):
            word = pick_random_word(length)
    return word

letters_is_known = []
def fill_in_letter(letter, word):
    for index in [pos for pos, char in enumerate(word) if char == letter]:
        fill_in_letter_at(index, letter)
        letters_is_known[index] = True

def word_guessed():
    for b in letters_is_known:
        if not b:
            return False
    return True

# run a full game from start to finish
def play_game(multiplayer_mode, length):
    letters_is_known = []
    word = get_word(multiplayer_mode, length)
    for i in range(len(word)):
        letters_is_known.append(' ' == word[i])
    
    # setup board
    setup_game(word)
    
    # ask for letters
    incorrect_guesses = 0
    while (True):
        letter = ask_for_guess()

        # deal with a guess
        if (letter not in word):
            # incorrect
            draw_body_part(incorrect_guesses)
            add_to_red_list(incorrect_guesses)
            incorrect_guesses = incorrect_guesses + 1
        else:
            # correct
            fill_in_letter(letter, word)
        
        # end conditions

        if (incorrect_guesses == 8):
            if(multiplayer_mode):
                player_two_wins()
            else:
                you_lose()
            break

        if (word_guessed()):
            if(multiplayer_mode):
                player_one_wins()
            else:
                you_win()
            break

# open the interface with just the initial pole
draw_hanger()

# determine initial mode to play in
multiplayer_mode = ask_if_multiplayer()
length = 0
if (not multiplayer_mode):
    length = ask_number_letters()
    
while(True):
    
    # play game
    play_game(multiplayer_mode, length)

    # ask if want to play again
    if (not play_again()):
        break

    wipe_shown_word()
    
    # change settings for next round
    if (change_settings()):
        multiplayer_mode = ask_if_multiplayer()
        if (not multiplayer_mode):
            length = ask_number_letters()

# game is stopped, close application
exit