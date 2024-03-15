#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from logo import logo
import random as rd

print(logo)
print("Welcome to the Number Guessing Game! ")
print("I am thinking of a number between 1 and 100.")
difficulty=input("Choose a difficulty type 'easy' or 'hard': ")
easy_attempts=10
difficult_attempts=5
endgame=False


def check (pc_number,player_number):
    if player_number>pc_number:
        print("Too high.")
    elif player_number<pc_number:
        print("Too low.")
    else:
        print(f"You got it! The answer was {pc_number}")
computer_nbr=rd.randint(1,100)

if difficulty=='easy':
    print(f"You have {easy_attempts} attempts remaining to guess the number")
    while(endgame==False):
        guess=int(input("Make a guess: "))
        check(computer_nbr,guess)
        easy_attempts-=1
        if easy_attempts==0:
            endgame=True
            print("Game Over, no more attempts")
        if computer_nbr==guess:
            endgame=True
        else:
            print(f"Guess again. \n You have {easy_attempts} attempts remaining to guess the number.")
elif difficulty=='hard':
    print(f"You have {difficult_attempts} attempts remaining to guess the number")
    while(endgame==False):
        guess=int(input("Make a guess: "))
        check(computer_nbr,guess)
        difficult_attempts-=1
        if computer_nbr==guess:
            endgame=True
        elif difficult_attempts==0:
            endgame=True
            print("Game Over, no more attempts")
        else:
            print(f"Guess again. \n You have {difficult_attempts} attempts remaining to guess the number.")






