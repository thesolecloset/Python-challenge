#Import the necessary libraries
import csv
import os

#Declare all variables needed
TotalVotes = 0
Candidates = []
CandidateNames = 0
CandidateVotes = {}
WinnerVotes = 0
Winner = ""
Results = ""
Votes = 0
VoterPercentage = 0

#Set the path of the CSV file that will have data pulled from
csvpath = "Resources/election_data.csv"

#Open the CSV File & Read Data From It As A Dictionary
with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
 
    #For loop to find the total number of votes & set candidate names row
    for row in csvreader:
        TotalVotes = TotalVotes + 1
        CandidateName = row["Candidate"]

        #If statement to loop for different candidate names in the csv & create a dictionary with names and votes
        if CandidateName not in Candidates:
            Candidates.append(CandidateName)
            CandidateVotes[CandidateName] = 1
        
        CandidateVotes[CandidateName] = CandidateVotes[CandidateName] + 1

#Declare the output file we want to write the results to & write to that file
#Print out the results to screen & write the same results to output file
output_file = "output.txt"
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    print ("Election Results")
    print ("")
    print ("-------------------------------")
    print ("")
    print (f'Total Votes:  {TotalVotes}')
    print ("")
    print ("-------------------------------")
    print ("")
    writer.writerow(["Election Results"])
    writer.writerow([])
    writer.writerow(["-------------------------------"])
    writer.writerow([])
    writer.writerow(["Total Votes: " + str(TotalVotes)])
    writer.writerow([])
    writer.writerow(["-------------------------------"])
    writer.writerow([])   
    
    #For loop to compare candidates votes and get the winner then print out the results and winner to screen and output file
    for CandidateName in CandidateVotes:
        Votes = CandidateVotes[CandidateName]
        VoterPercentage = float(Votes)/float(TotalVotes)*100
        if (Votes > WinnerVotes):
            WinnerVotes = Votes
            Winner = CandidateName
        Results = f'{CandidateName}: {VoterPercentage:.2f}% ({Votes})'
        print(f'{CandidateName}: {VoterPercentage:.2f}% ({Votes})')
        print ("")
        writer.writerow([Results])
        writer.writerow([])
    print ("-------------------------------")
    print ("")
    print (f'Winner: {Winner}')
    print ("")
    print ("-------------------------------")
    writer.writerow(["-------------------------------"])
    writer.writerow([]) 
    writer.writerow(["Winner: " + Winner]) 
    writer.writerow([])
    writer.writerow(["-------------------------------"])
    



    