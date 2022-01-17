import random

def generate_number(difficulty):
    return int(random.randrange(1, difficulty))

def  get_guess_from_user(difficulty):
    game_guess = input("Please insert a guess between 1 to " + str(difficulty) + " ")
    return int(game_guess)

def compare_results(difficulty):
    return generate_number(difficulty) == get_guess_from_user(difficulty)

def play(difficulty):
    return compare_results(difficulty)

#TEST
# if play(3) == True:
#     print('Won')
# else:
#     print ('Lost')