import os
import csv

poll_data = os.path.join("Resources", "election_data.csv")

def total_votes(poll_data):
    with open(poll_data, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        votes_cast = sum(1 for row in csv_reader if row[0])
        return votes_cast

def find_candidates_and_votes(poll_data):
    candidates = {}
    with open(poll_data, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            if len(row) > 2:  
                candidate_name = row[2]
                if candidate_name in candidates:
                    candidates[candidate_name] += 1
                else:
                    candidates[candidate_name] = 1
            else:
                print(f"Skipping row with insufficient columns: {row}")
    return candidates


all_votes = total_votes(poll_data)  
candidates_votes = find_candidates_and_votes(poll_data)

print(f"Election Results")
print(f"Total Votes: {all_votes}")
print(f"-------------------------")
winner = None
max_votes = 0

for candidate, votes in candidates_votes.items():
    percentage = (votes / all_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > max_votes:
        max_votes = votes
        winner = candidate

print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

winner = None
max_votes = 0

folder = 'analysis'
analysis_file = 'analysis.txt'
analysis_path = os.path.join(folder, analysis_file)

with open(analysis_path, 'w') as file:
    file.write("Election Results\n")
    file.write(f"Total Votes: {all_votes}\n")
    file.write("-------------------------\n")

    for candidate, votes in candidates_votes.items():
        percentage = (votes / all_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        if votes > max_votes:
            max_votes = votes
            winner = candidate

    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

