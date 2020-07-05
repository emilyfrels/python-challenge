# Import the os module
import os

# Import the module to read a csv file
import csv


# Set variable and location of csv file

csvpath = os.path.join('Resources', 'election_data.csv')

# Check to make sure the file path is correct
# print(csvpath)

# Set initial amount for total number of votes per candidate
total_votes = 0
vote_count = 0

# Create a dictionary to store all candidate info
candidates = {}



# Open the csv
with open(csvpath) as election_data:

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
    # print(candidates[name])

# Print header of output with formatting lines
print("Election Results")
print("------------------")

# Print total number of votes with formatting lines
print(f"Total Votes: {total_votes}")
print("------------------")

# Loop through to find the candidates and their vote counts and calculate percentage of the votes
    
for candidate_name, vote_count in candidates.items():
    percentage = (vote_count / total_votes) * 100
    # Print candidate name, percentage of votes, and number of votes
    print(f"{candidate_name}: " + "{:.3f}".format(percentage) + "%" + " (" + str(vote_count) + ")")


# Print formatting line for readability
print("------------------")


# print(total_votes)

# for candidate_name, vote_count in candidates_votes.items():
#     print(f"{candidate_name}: {vote_count}")

# print(candidates_votes)




