# Guessing games - oliver, calleigh, karla

import random
def generate_random_number():
    return random.randint(1,100)
print(generate_random_number)

def get_user_guess():
    while True:
        guess = int(input("enter your guess"))
        if guess >= 1 and guess <= 100:
            print(f"{guess} is a valid guess")
            return guess
        else:
            print(f"{guess} is invalid")

def play_gessing_game():
    secret_number = random.randint(1,100)
    while True:
        guess = get_user_guess()
        if guess == secret_number:
            print("correct")
            break
        else:
            print(f"wrong" )

play_gessing_game()