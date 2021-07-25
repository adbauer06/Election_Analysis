# Election_Analysis

## Project Overview
A Colorado Board of Elections employee had requested that an audit be performed on a recent local congressional election.  The following tasks were requested:

1.  Calculate the total number of votes cast.
1.  Get a complete list of candidates who recieved votes
1.  Calculate the total number of votes each candidate received.
1.  Calculate the percentage of votes each candidate won.
1.  Determine the winner of the election based on popular vote.

Upon submission of those metrics, I was then asked to expand upon that and add county-specific data also, specifically to:
1.  Calculate the voter turnout for each county.
1.  Calculate the percentage each county had of the total votes.
1.  Determine and report which county had the highest turnout (in relation to the total vote).

These results were to be reported both within the terminal upon running the audit program, as well as written to a text file.

##  Resources
The following resources were used to complete this analysis:
- Data Source:  election_results.csv, containing election data by county and voter ID
- Software:  Python 3.7.6, Visual Studio Code, 1.58.2

## Election Audit Results
The analysis of the election results shows that:
- There were 369,711 total votes cast in the election.
- The candidates who recieved votes were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 85,213 votes resulting in 23.0% of the vote.
    - Diana DeGette recieved 272,892 resulting in 73.8%" of the vote. 
    - Raymon Anthony Doane recieved 11,606 resulting in 3.1%" of the vote.
- The winner of the election according to popular vote was:
    - Diana DeGette with 272,892 votes and 73.8% of the total vote.

 The analysis of the county voting data shows the following:
 - Three counties were represented:
    - Jefferson county had 10.5% of the total votes with 38,855 votes.
    - Denver county had 82.8% of the total votes, with 306, 055 votes.
    - Arapahoe county had 6.7% of the total votes, with 24, 801 votes.
 - The county that had the highest number of votes was:
    - Denver County


 ## Election Audit Summary
 This particular election audit script was written to read a specific election results file for a county-level election.  However, with some minor modifications, it could be used for other elections also.  Below are a list of specific changes that could be made in order to use this for other elections.

### Change to Use a Different Input Source
This program is written to accept a specific file at a specific path.  The following line of code defines our input datasource.  This can be changed to add a different file name or path or both.

    file_to_load = os.path.join("Resources", "election_results.csv")


### Change to Read a File Formatted Differently
The program is written to process a voter results file where the first column is voter ID, the second column is the county, and the third column is the resulting vote.  The only two fields we need to reference and process are the level we are reporting results on (i.e. in this file it is county) and the voter result.  The following two lines are where these are defined:
        
    candidate_name = row[2]
    county_name = row[1]

In the current input file, candidate (or vote result) is defined as being in the third column, so indexed with 2.  The county name is the second column, therefore indexed with 1.  Those indexes can be changed to handle files that might have that data in different columns.

### Change to Process for a Different Geographical Area
This particular program was written specifically to process a file made up of county-level data.  However, the base logic would be the same whether we are reporting at a county-level, state-level, city-level, or other. While this specific change would not affect the overall logic,you would likely want to change the county-specific variable names to be more relatable to the data we are actually processing.  For example, the following list we declared for county, or the dictionary we declared to track votes by county:

    county_list = []
    county_votes = {}

could be changed to 

    city_list = []   or state_list = []
    city_votes = []  or state_votes = []

Also, our output report contains titles specifically for "County" that would also need to be changed within the code to accurately reflect the data being reported.  

    election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n\n"
            f"County Votes:\n")
        
    highest_county_summary = (
        f"\n-------------------------\n"
        f"Highest County Turnout: {highest_county}\n"
        f"-------------------------\n")

Instead of "County Votes" or "Highest county Turnout", you would want to change "county" to "state" or "city" or other to match the data being reported.



