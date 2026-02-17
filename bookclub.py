#Carmen V. Elston
#CSC 500 Week 5 Critical Thinking

#CSU Book Club Points
#The programmer assumes that there is a range of books for the level of points.
#Prompt the user to enter the numbr of books they purchased.
books = int(input("Enter the number of books purchased this month: "))

#The if statements starts the branching. If the number of books is 0 or 1 is True,
#Python runs the indented block and skips the rest of the checks.
if books <= 1:
    points = 0
#Python only checks here if books <= 1 is False and continues in this manner.
elif books <= 3:
    points = 5
elif books <= 5:
    points = 15
elif books <= 7:
    points = 30
#This runs if none of the previous conditions were True.
else:
    points = 60

print(f"You earned {points} points this month!")