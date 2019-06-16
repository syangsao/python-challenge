# Import the os module
import os
# Import the cvs module
import csv

## Import operator
## https://stackoverflow.com/questions/6193498/pythonic-way-to-find-maximum-value-and-its-index-in-a-list
import operator

# Path to budget_data csv file
# Note that we are in the same directory structure as this script
budget_csv = os.path.join ('.', 'budget_data.csv')

# Set the empty variables 
total_months = []
total_dollars = 0
average_change = []
increase_greatest = []
decrease_greatest = []
increase_month = []
decrease_month = []

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
        increase_greatest.append(increase)
        
        # the greatest decrease in profits
        decrease = int(row[1])
        decrease_greatest.append(decrease)

        # the greatest increase month
        testmax = (max(enumerate(increase_greatest), key=operator.itemgetter(1)))
                
        # the greatest decrease month
        testmin = (min(enumerate(decrease_greatest), key=operator.itemgetter(1)))

(max(increase_greatest)) #figure out the index, then apply it to the entire index/line for row[0]
(min(decrease_greatest)) #figure out the index, then apply it to the entire index/line for row[0]
                
#for index, value in enumerate(increase_greatest):
#    print(max(index, value))

### Use print statements below as a test only ###
        
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(len(total_months)))
print("Total: $" + str(total_dollars))       
# print("Average Change: " + (average_change))
print("Greatest Increase: " + "(" + str(max(increase_greatest)) + ")")
print("Greatest Decrease: " + "(" + str(min(decrease_greatest)) + ")")

# Set variable for output file
output_file = os.path.join("financial_analysis.txt")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)