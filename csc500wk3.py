#Carmen V. Elston
#CSC500 Week 3

#Part 1
# #This program calculates the total cost of a meal purchased.
#The user enters the charge for the food.
#Total cost is calculated at 18% tip and 7% sales tax.
#First, define variables and ask for user input.

food_cost = float(input('Enter food cost: '))
tip_18 = food_cost * 0.18
tax = food_cost * 0.07
total_cost = food_cost + tip_18 + tax

#Second, properly format and display the food cost, tip, and tax.
#:.2f ensures the currency is printed with two decimal places.
print(f'Food cost: ${food_cost:.2f}')
print(f'Tip (18%): ${tip_18:.2f}')
print(f'Sales tax (7%): ${tax:.2f}')
print(f'Total cost: ${total_cost:.2f}')

#Part 2
#This program calculates the alarm time based on user input.
#The user inputs the current time and hours to wait for the alarm.
#The program calculates on a 24-hour clock.

#First, the user inputs the current time and how many hours to wait.
current_time = int(input('Enter current time on a 24 hour clock (0-23): '))
hours_to_wait = int(input('Enter hours to wait: '))

#The modulo operator keeps the program on the 24-hour clock.
alarm = (current_time + hours_to_wait) % 24

print('The alarm will go off at', alarm)
