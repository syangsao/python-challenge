# import the os module
import os
# import the cvs module
import csv

# path to budget_data csv file
# Note that we are in the same directory structure as this script
budget_csv = os.path.join ('.', 'budget_data.csv')

# function
total_months = []
total_dollars = []
average_change = []
greatest_increase = []
greatest_decrease = []

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # calculate the amount of total monts
        
        # calculate the total amount in dollars
        
        # what the average change was
        
        # the greatest increase in profits 
        
        # the greatest decrease in profits
    