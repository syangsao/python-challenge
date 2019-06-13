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
##        total_months += 1
## https://dfrieds.com/python/read-in-csv-files
##        print(total_months)      
##        total_months.append(row[0])
        
        # calculate the total amount in dollars
        total_dollars += int(row[1])
#        total_dollars.append(row[1])
        
 ##       print(total_dollars)
        
        # what the average change was
        
        # the greatest increase in profits 
        
        # the greatest decrease in profits

        print("Financial Analysis")
        print("----------------------------")
        print("Total Months: " + str(len(total_months)))
        print("Total Dollars: " + str(total_dollars))
        
#        print("Average Change: " + (average_change))
#        print("Greatest Increase: " + (greatest_increase))
#        print("Greatest Decrease: " + (greatest_decrease))