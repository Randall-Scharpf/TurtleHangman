# find a word that the player will guess
def get_word(is_multiplayer):
    if (is_multiplayer):
        while True:
            word = request_word()
            display_word(word)
            if(ask_for_confirmation()):
                wipe_shown_word()
                break
            wipe_shown_word()
    else:
        length = ask_number_letters()
        while (len(word) != length):
            word = pick_random_word()
    return word

# run a full game from start to finish
def play_game(multiplayer_mode):
    word = get_word(multiplayer_mode)
    
    # setup board
    setup_game(len(word))
    
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
            fill_in_letter(letter)
        
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

while(True):
    
    # play game
    play_game(multiplayer_mode)

    # ask if want to play again
    if (not play_again()):
        break

    # change settings for next round
    if (change_settings()):
        multiplayer_mode = ask_if_multiplayer()

# game is stopped, close application
exit