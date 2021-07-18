# The date we need to retrieve:
# 1.  The total number of votes cast
# 2.  A complete list of candidates who recieved votes
# 3.  The percentage of votes each candidate won
# 4.  The total number of votes each candidate won
# 5.  The winner of the election based on popular vote

# Add our dependencies
import csv
import os

# Assign a variable to load a file form a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize the total vote counter.
total_votes = 0

# Initialize the candidate options list
candidate_options = []

# Create a dictionary to store votes by candidate
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #  Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Get the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate in the list...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

#Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results (Homework)\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
          
    # Determine the percentage of votes for each candidate 
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:

        # Retrieve the vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes
        vote_percentage = float(votes)/float(total_votes) * 100

        # Print the candidate name and percentage of votes.
        # print(f"{candidate_name}: recieved {vote_percentage:.1f}% of the vote.")

        # Determine the winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And set the winning_candidate equal to candidate's name
            winning_candidate = candidate_name

        # Print out each candidate's name, vote count, and percentage of votes to the terminal
        # print (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their vote count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

    # Print out the winning candidate, vote count, and percentage to terminal
    winning_candidate_summary = (
        f"---------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate info to our text file.
    txt_file.write(winning_candidate_summary)
