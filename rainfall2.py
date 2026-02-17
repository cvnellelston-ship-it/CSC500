#Carmen V. Elston
#CSC 500 Week 5 Critical Thinking

#Rainfall Problem
#This program collects monthly rainfall over a period of months
#It then calculates the total months, total rainfall, and average rainfall per month.

#The user enters the number of years of data.
years = int(input("Enter the number of years: "))

#The loop initializes here.
#Total inches of rainfall over all years
total_rainfall = 0.0
#Total number of months
total_months = 0

#This outer loop runs once for each year.
for year in range(years):
    for month in range(12):
        rainfall = float(input(f"Enter rainfall for Year {year +1}, Month {month +1}: "))
        total_rainfall += rainfall
        total_months += 1

average_rainfall= total_rainfall / total_months

print("\nRESULTS")
print(f"Total months: {total_months}")
print(f"Total rainfall (inches): {total_rainfall:.2f}")
print(f"Average rainfall (inches): {average_rainfall:.2f}")