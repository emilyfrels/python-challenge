# Import the os module
import os

# Import the module to read a csv file
import csv


# Set variable and location of csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# Set variable and location of output text file
output_path = os.path.join('analysis', 'poll_analysis.txt')

# Set initial amount for total number of votes per candidate
total_votes = 0
vote_count = 0

# Create a dictionary to store all candidate info
candidates = {}


# Open the csv and open the ouput texttfile
with open(csvpath) as election_data, open(output_path, 'a') as txtfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(election_data, delimiter=',') 

    # Check to make sure file is being read
    # print(election_data)

    # Print a title and a spacer
    
    # Skipping the header in the csv
    csv_header = next(csvreader)



    # Find the complete list of candidates who received votes
    # Start by looping through each row
    for row in csvreader:

        # Calculate total number of votes
        total_votes = total_votes + 1
        
        # Create a list to store candidates names
        name = row[2]

        if name not in candidates:
            # If name not in list of candidates, add it to the candidate list
            candidates[name] = 1
        else:
            # Track number of votes per candidate name
            candidates[name] = candidates[name] + 1


# Print header of output with formatting lines
print("Election Results")
print("------------------")


# Print total number of votes with formatting lines
print(f"Total Votes: {total_votes}")
print("------------------")



for candidate_name, vote_count in candidates.items():
    # Calculate the percentage of votes per candidate
    percentage = (vote_count / total_votes) * 100
    # Print candidate name, percentage of votes, and number of votes
    print(f"{candidate_name}: " + "{:.3f}".format(percentage) + "%" + " (" + str(vote_count) + ")")

# Find the max value of votes by sorting the values in the vote count list
sorted_values = sorted(candidates.values(), reverse=True)
#print(sorted_values)
#print(sorted_values[0])

# Assign variable to the largest number
winner = sorted_values[0]
# print(winner)

# print(vote_count)

# Loop through to find if the largest vote count value matches any of the vote counts and display the winner
for candidate_name, vote_count in candidates.items():

    if vote_count == winner:
        # Print results
        print("------------------")
        print(f"Winner: {candidate_name}")
        print("------------------")








