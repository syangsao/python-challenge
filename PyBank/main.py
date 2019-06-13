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
        print(row)
        # calculate the amount of total months
        
        # calculate the total amount in dollars
        
        # what the average change was
        
        # the greatest increase in profits 
        
        # the greatest decrease in profits
    