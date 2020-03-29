#The data we need to retrieve.
#1. The total number of votes cast
#2. The complete list of candidates who received votes
#3 The percentage of votes each candidate won
#4 The total number of votes each candidate won
#5 The winner of election based on popular vote

#Add our dependencies
import os
import csv
#Assigning variable for file to load and the path
file_to_load = os.path.join('Resources/election_results.csv')
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

#County list
county_options = []
#County dictionary
county_votes = {}

largest_turnout = ''
county_count = 0
county_percentage = 0

# Winning Candidate and Winning Count Tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0

#open the election results and read the file.
with open(file_to_load) as election_data:
    #Read file object with reader fn
    file_reader = csv.reader(election_data)

    #Print the header row.
    headers = next(file_reader)
    print(headers)

    for row in file_reader:
        total_votes += 1
    
        # Print the candidate name from each row
        candidate_name = row[2]

        # If candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add candidate name to the candidate list.
            candidate_options.append(candidate_name)

            #2. Begin tracking that candidate's vote count by setting count to 0.
            candidate_votes[candidate_name] = 0

        #3. Add a vote to the candidate's count.
        candidate_votes[candidate_name] += 1
        
        # Print the county name from each row
        county_name = row[1]

        # If candidate does not match any existing candidate...
        if county_name not in county_options:
            # Add candidate name to the candidate list.
            county_options.append(county_name)

            #2. Begin tracking that candidate's vote count by setting count to 0.
            county_votes[county_name] = 0

        #3. Add a vote to the candidate's count.
        county_votes[county_name] += 1
# Using the open() fn w the 'w' mode, we will write data to the file.
with open(file_to_save, 'w') as txt_file:

# Print the final vote count to the terminal.
    election_analysis = (
        f'\nElection Results\n'
        f'------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'------------------------\n')
    print(election_analysis, end='')
    #Save the final vote count to the text file.
    txt_file.write(election_analysis)
    print('County Votes:')     
    for county in county_votes:
        votes = county_votes[county]
        vote_percentage = int(votes)/int(total_votes)*100
        county_results = (f'{county}:{vote_percentage:.1f}% ({votes:,})\n')
        print(county_results)
        txt_file.write(county_results)
        if (votes > county_count) and (vote_percentage > county_percentage):
            #B) If true then set county_count = votes, w_% = v_%
            county_count = votes
            county_percentage = vote_percentage
            #And, set the largest_turnout = county name
            largest_turnout = county
    county_analysis = (f'\n'
    f'---------------------------\n'
    f'Largest County Turnout: {largest_turnout}\n'
    f'---------------------------')
    print(county_analysis)
    txt_file.write(county_analysis)

    #Determine % of votes for each candidate by looping through the counts
    #A)Iterate thru the candidate list.
    for candidate in candidate_votes:
        #B) Retrieve vote count of ea cand.
        votes = candidate_votes[candidate]
        #C) Calc % of votes
        vote_percentage = int(votes)/int(total_votes)*100
        candidate_results = (f'{candidate}:{vote_percentage:.1f}% ({votes:,})\n')
        #print results
        print(candidate_results)
        #Write into txt
        txt_file.write(candidate_results)
    #Determine winning vote count and candidate
        #A) Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #B) If true then set winning_count = votes, w_% = v_%
            winning_count = votes
            winning_percentage = vote_percentage
            #And, set the winning_candidate = candidate name
            winning_candidate = candidate

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

#Close the file.
election_data.close()


