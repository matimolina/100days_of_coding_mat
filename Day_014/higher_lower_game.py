import random as rd
from art import logo, vs
from game_data import data

score=0
print(logo)
a=rd.randint(0,len(data))
print(f"Compare A: {data[a]['name']}, {data[a]['description']}, from {data[a]['country']}. ")
print(vs)
b=rd.randint(0,len(data))
print(f"Against B: {data[b]['name']}, {data[b]['description']}, from {data[b]['country']}. ")
choice=input("Who has more followers? Type 'A' or 'B': ").lower()
decisions={'a':a,'b':b}
print(choice)
print(data[decisions[choice]])

def win(choice,computer):
    if data[choice]['follower_count']>data[computer]['follower_count']:
        return 1
    else:
        return -1

win(choice,b)


