# import modules
import csv
import os

# set the path to the file
pypoll_csv = os.path.join(".","election_data.csv")

# variable lists
candidate = []
votes = []
name = []

# open csv file and skip the first row
with open(pypoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        candidate.append(row[2])

    candidate_count = [[x,candidate.count(x)] for x in set(candidate)]
        
    for row in candidate_count:
        name.append(row[0])
        votes.append(row[1])

    candidate_zip = zip(name, votes)
    candidate_list = list(candidate_zip)

    winner = max(votes)

    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]       
            
total_votes = len(candidate)

correy_total = candidate.count('Correy')
correy_percent = int(correy_total) / int(total_votes)

o_tooley_total = candidate.count("O'Tooley")
o_tooley_percent = o_tooley_total / total_votes

li_total = candidate.count('Li')
li_percent = li_total / total_votes

khan_total = candidate.count('Khan')
khan_percent = khan_total / total_votes

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(f'Khan: {khan_percent:.3%} ({khan_total})')
print(f'Correy: {correy_percent:.3%} ({correy_total})')
print(f'Li: {li_percent:.3%} ({li_total})')
print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})")
print(f'-------------------------')
print(f'Winner: {winner_name}')
print(f'-------------------------')

with open('pypoll.txt', 'w') as text_file:
    print(f'Election Results', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Total Votes: {total_votes}', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Khan: {khan_percent:.3%} ({khan_total})', file=text_file)
    print(f'Correy: {correy_percent:.3%} ({correy_total})', file=text_file)
    print(f'Li: {li_percent:.3%} ({li_total})', file=text_file)
    print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})", file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Winner: {winner_name}', file=text_file)
print(f'-------------------------', file=text_file)