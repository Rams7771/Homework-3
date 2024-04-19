import os
import csv

budget_data_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

#I decided to set all the variables at the beginning 
# This way of starting off my coding was shared by Melissa Judy during one of our class work sessions. 
total_months = 0
net_profits = 0
current_profit = 0
previous_month = 0
max_value = float('-inf')
max_date = None
min_value = float("inf")
min_date = None
total_change_in_profit = 0
is_first_row = True

#Open/Read CSV
with open(budget_data_csv, encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#Skip Header
    csv_header = next(csv_file)

#Find months and profit/losses
    for row in csv_reader:
        last_month_profit = current_profit
        total_months += 1
        current_profit = float(row[1])
        net_profits += current_profit

#Largest Increase in Profits
    date = row[0]
    change_in_profit = current_profit - last_month_profit
    if not is_first_row:
        total_change_in_profit += change_in_profit
    else:
        is_first_row = False

    if change_in_profit > max_value:
        max_value = change_in_profit
        max_date = date

#Largest Decrease
        date = row[0]
    if change_in_profit < min_value:
        min_value = change_in_profit
        min_date = date
#Average of changes
    average = total_change_in_profit/(total_months-1)

#print analysis to terminal
#this portion of my code was shared by Chelsean Cullens/Melissa Judy in cooperation with a tutor that Chelsea worked with. 
    Analysis_summary = "Financial Analysis"
    Analysis_summary = "--------------------------------------------------------\n"
    Analysis_summary+=f'total_months= {total_months}\n'
    Analysis_summary+=f'Total= ${net_profits}\n'
    Analysis_summary+=f'Average= ${average}\n'
    Analysis_summary+=f'Largest Increase in Profits= {max_date} (${max_date})\n'
    Analysis_summary+=f'Largest Decrease in Profits= {min_date} (${min_value})\n'
    print (Analysis_summary)
#Export to text file
#This was shared by Caleb Cutrer and his research on stackflow
    output = os.path.join('PyBank', 'Analysis', 'Bank_analysis.txt')
    with open(output, "w", newline='') as datafile:
        writer = csv.writer(datafile)

        print("Financial Analysis", file=datafile)
        print(Analysis_summary, file=datafile)








