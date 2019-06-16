# Import the os module
import os
# Import the cvs module
import csv

# Path to budget_data csv file
# Note that we are in the same directory structure as this script
budget_csv = os.path.join ('.', 'budget_data.csv')

# Set the empty variables 
total_months = []
total_dollars = 0
average_change = []
greatest_increase = []
greatest_decrease = []

with open(budget_csv, newline="") as csvfile:
    
    # CSV reader specifies delimiter and variable that holds the contents
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # This skips the first row (From 3-2-07)
    csv_header = next(csvreader) 

    for row in csvreader:
        # calculate the amount of total months
        total_months.append(row[0])
        
        # calculate the total amount in dollars
        total_dollars += int(row[1])
                
        # what the average change was
        change = int(row[1]) + 2  
        average_change.append(change)
        
        # the greatest increase in profits 
        increase = int(row[1])
        greatest_increase.append(increase)
        
        # the greatest decrease in profits
        decrease = int(row[1])
        greatest_decrease.append(decrease)

        # the greatest increase month
        
        # the greatest decrease month
                
### Use print statements below as a test only ###
        
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(len(total_months)))
print("Total: $" + str(total_dollars))       
# print("Average Change: " + (average_change))
print("Greatest Increase: " + "(" + str(max(greatest_increase)) + ")")
print("Greatest Decrease: " + "(" + str(min(greatest_decrease)) + ")")