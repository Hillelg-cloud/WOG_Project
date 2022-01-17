from currency_converter import CurrencyConverter
import random

def get_money_interval(difficulty, guess, currency):
    currency   = float(currency)
    difficulty = int(difficulty)
    guess      = float(guess)
    if guess < (currency + difficulty) and guess > (currency - difficulty):
        return True
    return False

def get_guess_from_user(amount):
    guess = input('Insert your currency guess for ' + str(amount) + ' USD in ILS ')
    if guess.isnumeric() == False:
        return 0
    return guess

def get_random():
    return int(random.randrange(1, 100))

def get_updated_currency(amount):
    c = CurrencyConverter()
    return c.convert(amount,'USD','ILS')

def play(difficulty):
    amount = get_random()
    user_guess = get_guess_from_user(amount)
    currency   = get_updated_currency(amount)
    print('The real currency is ' + str(currency))
    return get_money_interval(difficulty, user_guess, currency)

# print(play(5))