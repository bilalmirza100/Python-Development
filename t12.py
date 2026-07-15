import random

easy_turns = 10
hard_turns = 5

def set_mode():
    mode = input("Choose a Mode. Type 'Easy' or 'Hard': ").lower()
    if mode == 'hard':
        print(f"You have {hard_turns} Attempts!")
        return hard_turns
    else:
        print(f"You have {easy_turns} Attempts!")
        return easy_turns

def check_answer(guess, answer, turns):
    """Compares the user's guess against the actual answer."""
    if guess > answer:
        print("Too High!")
        return turns - 1
    elif guess < answer:
        print("Too Low!")
        return turns - 1
    else:
        print(f"You have got it! The answer is {answer}")
        return 0

def game():
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    
    turns = set_mode()
    
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        
        guess = int(input("Make a guess: "))
        
        turns = check_answer(guess, answer, turns)
        
        if turns == 0:
            if guess != answer:
                print("You have run out of guesses, You lose.")
            return
        elif guess != answer:
            print("Guess Again.")


game()