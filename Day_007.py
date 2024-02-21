###Hangman
#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word=random.choice(word_list)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')
display=[]
for i in chosen_word:
    display+='_'
print(display)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess=input("guess a letter \n").lower()

for i in range(len(chosen_word)):
    letter=chosen_word[i]
    if letter ==guess:
        display[i]=letter

print(display)
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

