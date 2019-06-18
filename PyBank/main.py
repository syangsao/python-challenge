# import modules
import os
import csv

# set the path to the file
budget_csv = os.path.join(".","budget_data.csv")

# variable lists 
profit = []
monthly_changes = []
date = []
count = 0
total_dollars = 0
total_change_profits = 0
initial_profit = 0

# open csv file
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # for loop in the reader
    for row in csvreader:    
      # count the # of months
      count = count + 1 
      date.append(row[0])

      # append and count the profit
      profit.append(row[1])
      total_dollars += int(row[1])

      # average change in profits from month to month and calulate the average change in profits
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

      # store the monthly changes in a list
      monthly_changes.append(monthly_change_profits)
      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit

      # figure out the average change 
      average_change_profits = (total_change_profits/count)
      
      # figure out the max and min change 
      greatest_increase = max(monthly_changes)
      greatest_decrease = min(monthly_changes)
      increase_date = date[monthly_changes.index(greatest_increase)]
      decrease_date = date[monthly_changes.index(greatest_decrease)]
      
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_dollars))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease)+ ")")

with open('financial_analysis.txt', 'w') as text:
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_dollars) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease) + ")\n")
