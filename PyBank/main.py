# Import the os module
import os
# Import the cvs module
import csv

# Path to budget_data csv file
# Note that we are in the same directory structure as this script
budget_csv = os.path.join ('.', 'budget_data.csv')

# Set the empty variables 
total_months = []
total_dollars = []
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
        months = row[0]
        total_months.append(months)
        
        # calculate the total amount in dollars
        
        # what the average change was
        
        # the greatest increase in profits 
        
        # the greatest decrease in profits

        print("Financial Analysis")
        print("----------------------------")
        print("Total Months: " + str(len(total_months)))
#        print("Total Months: " + str(len(total_months)))
#        print("Total: " + (total_dollars))
#        print("Average Change: " + (average_change))
#        print("Greatest Increase: " + (greatest_increase))
#        print("Greatest Decrease: " + (greatest_decrease))
