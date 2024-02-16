print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0

if height>120:
    print("You can ride the rollercoster!")
    age=int(input("What is your age? "))
    if age<12:
        bill=5
        print("Child tickets are $5.")
    elif age<=18:
        bill=7
        print("Youth tickets are $7.")
    elif age>=45 and age<=55:
        print("Have a free ride on us. ")
        bill=0
    else:
        bill=12
        print("Adult tickets are $12.")
    wants_photo=str(input("Do you want a photo taken? Y or N. "))
    if wants_photo=="Y":
        bill+=3
    print(f"Your final bill is ${bill}. ")
else:
    print("Sorry, you have to grow taller before you can ride.")

###Treausere Island

print('''
.
|\
|X\
 XX\         _    O_/
  XX\    o  (#)==_/\
   XX\             /\/
    XX\           /
     XX\.
      XX|
ejm97  X|
      ''')

print("Welcome to Treasure Island. ")
print("Your mission is to find the treasure. ")
l_r=input("Where do you want to go? Left or right? ").lower()

if l_r=="left":
    #CONTINUE THE GAME
    s_w=input("What do you want to do? Swim or wait? \n").lower()
    if s_w=="wait":
        door=input("Which door do you want to select? Red, blue or yellow? \n").lower()
        if door=="red":
            print("Burned by fire.Game Over.")
        elif door=="blue":
            print("Eaten by beasts.Game Over.")
        elif door=="yellow":
            print("You win!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Attacked by trout.Game Over.")
