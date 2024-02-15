#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
input("Welcome to the tip calculator.")
bill=input("how much was the total bill? $")
tip=input("what percentage tip would you like to give? 10, 12, or 15? ")
people=input("how many people to split the bill? ")

total=float(bill)*float(tip)/100+float(bill)
split=round(total/float(people),2)
print(f"each person should pay: ${split}")