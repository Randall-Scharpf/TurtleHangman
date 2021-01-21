# TurtleHangman
West High AP Computer Science Period 3 Group 10 Semester 1 Final Project. This is an interactive game of hangman.

## Setup
This program runs on Python. You must have the language utilities installed on your system to play. You can check whether or not your computer is set up by running `python --version` in your system's terminal. If Python is not installed, check the downloads page https://www.python.org/downloads/ to find the correct version for your system.  
Running main.py will launch TurtleHangman. For Windows systems, the end user does not need to manually compile and run the Python program from a terminal or IDE and can instead use the utilities bundled with the releases (https://github.com/Randall-Scharpf/TurtleHangman/releases) to compile and run the program. Instructions for the compilation utilities are listed as the description for each individual release. There are not yet any releases for MacOS or *nix systems.

## Playing TurtleHangman
Two windows will open - the console interface by which player(s) interact with the program and the graphical interface by which the program interacts with the player(s). To begin, the interface will ask for settings. Then, the game begins. If you are playing the two-player game, have the other player step away while you choose a word. Once your settings are picked, let the guessing begin! Each letter that is correctly guessed brings you closer to finding the word, but each letter incorrectly guessed brings another strike toward your loss! If you can guess the whole word before racking up eight strikes, you win!  
You can play the game over and over with the same settings, or you can change settings before you play again, or you can just play once. The choice is yours!

## Change Log
1.0 - Implements functional one-player and two-player games. Potential feature requests: save progress and persistent statistics, password-style two-player console word-choosing interface