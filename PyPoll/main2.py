import csv 

total_votes = 0
charles_total= 0
charles_total_percent = 0
diana_total = 0
diana_total_percent = 0
raymon_total = 0
raymon_total_percent = 0
winner = ""
winning_vote = 0

csv_path = "/Users/Xenos/Desktop/PythonChallenge/python-challenge/PyPoll/Resources/election_data.csv"
output_file = "/Users/Xenos/Desktop/PythonChallenge/python-challenge/PyPoll/poll_data.txt"
with open(csv_path) as election_data:
    csv_reader = csv.reader(election_data, delimiter= ",")
    election_header = next(csv_reader)
    print(election_header)

    for row in csv_reader:
        total_votes += 1

        if row [2] == "Charles Casper Stockham":
            charles_total += 1
        elif row[2] == "Diana DeGette":
            diana_total +=1
        elif row[2] == "Raymon Anthony Doane":
            raymon_total += 1   

charles_total_percent = (charles_total/total_votes) * 100
diana_total_percent = (diana_total/total_votes) * 100
raymon_total_percent = (raymon_total/total_votes) * 100

winning_vote = max(charles_total, diana_total, raymon_total)
if winning_vote == charles_total:
    winner = "Charles Casper Stockham"
elif winning_vote == diana_total:
    winner = "Diana DeGette"
elif winning_vote == raymon_total:
    winner = "Raymon Anthony Doane"

print("Election Results:")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
print(f"Charles Casper Stockham: {charles_total_percent}% ({charles_total})")
print(f"Diana DeGette: {diana_total_percent}% ({diana_total})")
print(f"Raymon Anthony Doane: {raymon_total_percent}% ({raymon_total})")
print("-----------------------------")
print(f"Winner: {winner}")
print("-----------------------------")

with open(output_file, 'w') as poll_file:
    poll_file.write("Election Results:\n")
    poll_file.write("-----------------------------\n")
    poll_file.write(f"Total Votes: {total_votes}\n")
    poll_file.write("-----------------------------\n")
    poll_file.write(f"Charles Casper Stockham: {charles_total_percent}% ({charles_total})\n")
    poll_file.write(f"Diana DeGette: {diana_total_percent}% ({diana_total})\n")
    poll_file.write(f"Raymon Anthony Doane: {raymon_total_percent}% ({raymon_total})\n")
    poll_file.write("-----------------------------\n")
    poll_file.write(f"Winner: {winner}\n")
    poll_file.write("-----------------------------\n")

print("poll_file has been saved to 'poll_data.txt'")
