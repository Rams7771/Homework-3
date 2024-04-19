import os
import csv

election_data_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')


#Variables 
total_votes = 0
winning_candidate = 0
max_percent = 0

#Open/Read CSV
with open(election_data.csv, encoding='UTF-8') as csv file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#Skip Header
    csv_header = next(csv_file)

#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won
Stockham_percent = Stockham/total_votes*100
DeGette_percent = DeGette/total_votes*100
Doane_percent = Doane/total_votes*100
#The total number of votes each candidate won
    for row in csv_reader:
        total_votes +=1
        candidates_names = row[2]
        if candidates_names not in candidate_choices:
            candidate_choices.add(candidates_names)
            candidates_running += 1

#The winner of the election based on popular vote


#print analysis to terminal. Please note I was using the same portion of code from PyBank but wasn't able to change the details to fit PyPoll. The idea was to summarize the election results, print to the terminal and create a text file in the analysis folder using the same method as I did in PyBank. 
#this portion of my code was shared by Chelsean Cullens/Melissa Judy in cooperation with a tutor that Chelsea worked with. 
    Analysis_summary = "Financial Analysis"
    Analysis_summary = "--------------------------------------------------------\n"
    Analysis_summary+=f'total_months= {total_months}\n'
    Analysis_summary+=f'Total= ${net_profits}\n'
    Analysis_summary+=f'Average= ${average}\n'
    Analysis_summary+=f'Largest Increase in Profits= {max_date} (${max_date})\n'
    Analysis_summary+=f'Largest Decrease in Profits= {min_date} (${min_value})\n'

#Export to text file
#This was shared by Caleb Cutrer and his research on stackflow
    output = os.path.join('Analysis', 'Bank_analysis')
    with open(output, "w", newline='') as datafile:
        writer = csv.writer(datafile)

        print("Financial Analysis", file=datafile)
        print(Analysis_summary, file=datafile)
