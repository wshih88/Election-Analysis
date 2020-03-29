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

#open the election results and read the file.
with open(file_to_load) as election_data:
    #Read file object with reader fn
    file_reader = csv.reader(election_data)

    #Print the header row.
    headers = next(file_reader)
    print(headers)

    #Printing Specific columns
    #for row in file_reader:
    
        #print(0)
    
    #print(election_data)



# Using the open() fn w the 'w' mode, we will write data to the file.
with open(file_to_save, 'w') as txt_file:

    txt_file.write('Counties, in, the, Election\n------------------------------\nArapahoe\nDenver\nJefferson')







#Close the file.
election_data.close()


