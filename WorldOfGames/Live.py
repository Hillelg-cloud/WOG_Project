import MemoryGame
import GuessGame
import CurrencyRouletteGame as Currency_Roulette


def welcome(name):
    return ("Hello " + name + " and welcome to the World of Games (WoG). \n"
                             + "Here you can find many cool games to play.")
def load_game():
    print("Please choose a game to play: \n"
          + "   1. Memory Game - a sequence of numbers will appear for 1 second and you have to \n"
          + "guess it back \n   2. Guess Game - guess a number and see if you chose like the computer \n"
          + "   3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    game_number = int(input(""))
    while (int(game_number) < 1 or int(game_number) > 3):
        game_number = input("Invalid game number please insert a valid game number ")
    game_difficulty = input("Please choose game difficulty from 1 to 5 ")
    while (int(game_difficulty) < 1 or int(game_difficulty) > 5):
        game_difficulty = input("Please choose game difficulty from 1 to 5 ")

    match game_number:
        case 1:
            if (MemoryGame.play(int(game_difficulty)) == True):
                print('You won')
            else:
                print('You lost')
        case 2:
            if (GuessGame.play(int(game_difficulty)) == True):
                print('You won')
            else:
                print('You lost')
        case 3:
            if (Currency_Roulette.play(int(game_difficulty)) == True):
                print('You won')
            else:
                print('You lost')

# Function Update
# 1. Change the function load_game() from the previous document that after it will get the
# user’s game of choice and level of difficulty, it will start a new function of the
# corresponding game with the given difficulty. For example: If a user will choose the first
# option in load_game() function with difficulty 3, it will call the play() function from the
# module MemoryGame with difficulty of 3.
# 2. Change the 3rd game description on load_game() function to: Currency Roulette - try
# and guess the value of a random amount of USD in ILS