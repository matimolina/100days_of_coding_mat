import random 

random_integer=random.randint(1,10)
print(random_integer)

random_float = random.random()*5
print(random_float)

random_coin=random.randint(0,1)

if random_coin==1:
    print("Heads")
else:
    print("Tails")


names=["Angela, Ben, Jenny, Michael, Chloe"]
names_list=names.split(", ")
a=len(names)
random_selection=random.randint(0,a-1)
select_person=names[random_selection]
print(f"{select_person} is going to buy the meal today!")


####Rock-Paper-Scissons
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
lista=[rock,paper,scissors]
list=["rock", "paper", "scissors"]
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
pc_choice=random.randint(0,2)

print(lista[choice])
print(f"Computer choice: {pc_choice}")
print(lista[pc_choice])

if list[choice]==list[pc_choice]:
    print("It is a draw")
elif list[choice]=="rock" and list[pc_choice]=="paper":
    print("You loose!")
elif list[choice]=="rock" and list[pc_choice]=="scissors":
    print("You win!")
elif list[choice]=="paper" and list[pc_choice]=="rock":
    print("You win!")
elif list[choice]=="paper" and list[pc_choice]=="scissors":
    print("You loose!")
elif list[choice]=="scissors" and list[pc_choice]=="rock":
    print("You loose!")
elif list[choice]=="scissors" and list[pc_choice]=="paper":
    print("You win!")
else:
    print("You typed an invalid number, you loose!")

