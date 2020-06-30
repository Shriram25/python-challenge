import os
import csv

csvpath = os.path.join('Resources','election_data.csv')
totalvotes = 0
candidates = []
uniquecandidates = []
votes = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    csv_header = next(csvreader)
    for row in csvreader:
        candidates.append(row[2])
        totalvotes = totalvotes +1
        
    for k in range (0, len(candidates)):
        if candidates[k] not in uniquecandidates:
            uniquecandidates.append(candidates[k])

    for j in range(0, len(uniquecandidates)):
        votes.append(candidates.count(uniquecandidates[j]))

        


maxloc = votes.index(max(votes))
winner = uniquecandidates[maxloc]

print("Election Results")
print("----------------------------")
print(f"Total Votes: {totalvotes}")

print("----------------------------")
for j in range(0,len(uniquecandidates)):
    print(f"{uniquecandidates[j]}: {votes[j]*100/totalvotes :.3f}% ({votes[j]}) ")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")







