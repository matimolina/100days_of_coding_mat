###Hangman
#Step 1
import random
from hangman_words import word_list

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word=random.choice(word_list)
word_length = len(chosen_word)

end_game=False
lives=6

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
from hangman_art import logo, stages
print(logo)


#Testing code
print(f'Pssst, the solution is {chosen_word}.')
display=[]

for i in chosen_word:
    display+='_'
print(f"{' '.join(display)}")

while end_game==False:
    guess=input("guess a letter \n").lower()
    if guess in display:
        print(f"You have already chosen this letter {guess}. ")
    for i in range(len(chosen_word)):
        letter=chosen_word[i]
        if letter ==guess:
            display[i]=letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives-=1
        if lives==0:
            end_game=True
            print("You loose")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    if '_' not in display:
        end_game=True
        print("You Win.")
    # Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
